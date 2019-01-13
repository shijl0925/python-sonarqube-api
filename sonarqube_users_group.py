#!/usr/bin/env python
	# -*- coding:utf-8 -*-
	
	"""
	这个脚本用于同步gitlab组、成员权限到sonarqube
	"""
	
	from sonarqube_utils.base_api import SonarAPIHandler
	import multiprocessing
	import sys
	import os
	from utils.common import get_json_data
	import pymysql
	import gitlab
	from utils.gitlab_service import gitlab_service, get_gitlab_projects_select_members, get_gitlab_groups_select_members, get_gitlab_users_info
	import time
	try:
	    reload(sys)
	    sys.setdefaultencoding('utf-8')
	except:
	    pass
	
	sonardb_config = {
	    'host': '*.*.*.*',
	    'port': 3306,
	    'user': 'sonar',
	    'password': 'sonar',
	    'db': 'sonar',
	    'charset': 'utf8mb4',
	    'cursorclass': pymysql.cursors.DictCursor,
	    }
	
	def project_role_groups(cursor, project_key, role):
	    """
	    检查项目中组权限
	    :param project_key:
	    :param role:
	    :return:
	    """
	    cursor.execute('SELECT id from projects where qualifier = "TRK" and kee = "{}";'.format(project_key))
	    resource_id = cursor.fetchall()[0]['id']
	
	    cursor.execute('SELECT group_id from group_roles where resource_id = {} and role = "{}" ;'.format(resource_id, role))
	    group_ids = [i['group_id'] for i in cursor.fetchall()]
	
	    group_names = []
	    for group_id in group_ids:
	        cursor.execute('SELECT name from groups where id = {};'.format(group_id))
	        group_name = cursor.fetchall()[0]['name']
	        group_names.append(group_name)
	
	    return group_names
	
	def project_role_users(cursor, project_key, role):
	    """
	    检查项目中用户权限
	    :param project_key:
	    :param user_name:
	    :param role:
	    :return:
	    """
	    cursor.execute('SELECT id from projects where qualifier = "TRK" and kee = "{}";'.format(project_key))
	    resource_id = cursor.fetchall()[0]['id']
	
	    cursor.execute('SELECT user_id from user_roles where resource_id = {} and role = "{}" ;'.format(resource_id, role))
	    user_ids = [i['user_id'] for i in cursor.fetchall()]
	
	    user_logins = []
	    for user_id in user_ids:
	        cursor.execute('SELECT login from users where id = {};'.format(user_id))
	        user_login = cursor.fetchall()[0]['login']
	        user_logins.append(user_login)
	
	    return user_logins
	
	def sonarqube_project_operate_func(sonarhandler, project_key, project_info):
	    """
	    :param sonarhandler:
	    :param project_key:
	    :param project_info:
	    :return:
	    """
	    permissions = ['codeviewer', 'user']
	    gitlab_url = "http://git.*.work"
	    jenkins_url = "http://sonar.jenkins.*.work"
	
	    group_name = project_info['group_name']
	    path = project_info['gitlab_project_path']
	    members = project_info['user_name']
	    visibility = project_info['visibility']
	    exist_permissions = project_info['exist_permissions']
	
	    # 置为私有项目
	    if visibility == 'public':
	        print("visibility")
	        sonarhandler.projects.update_project_visibility(project_key, 'private')
	        print('update project {} visibility status private'.format(project_key))
	
	    if 'sonar-users' not in exist_permissions['user']['groups']:
	        sonarhandler.permissions.project_permissions_add_group(project_key, 'sonar-users', 'user')
	        print('add group {} to project {} successful, permission: {}'.format('sonar-users', project_key, 'user'))
	
	    for permission in permissions:
	        # 给项目添加用户组权限
	        if group_name not in exist_permissions[permission]['groups']:
	            sonarhandler.permissions.project_permissions_add_group(project_key, group_name, permission)
	            print('add group {} to project {} successful, permission:{}'.format(group_name, project_key,
	                                                                                    permission))
	        # 给项目添加用户权限
	        sonar_project_members = exist_permissions[permission]['users']
	
	        need_add_users_to_sonar_project = list(set(members) - set(sonar_project_members))
	        need_delete_users_from_sonar_project = list(set(sonar_project_members) - set(members))
	
	        # 需要添加到sonarqube项目中的用户
	        for m in need_add_users_to_sonar_project:
	            sonarhandler.permissions.project_permissions_add_user(project_key, m, permission)
	            print('add member {} to project {} successful, permission: {}'.format(m, project_key, permission))
	
	        # 需要从sonarqube项目中删除的用户
	        for m in need_delete_users_from_sonar_project:
	            sonarhandler.permissions.project_permissions_remove_user(project_key, m, permission)
	            print('delete  member {} from project {} successful, permission: {}'.format(m, project_key, permission))
	
	    # 给项目添加链接
	    links_name = []
	    project_links_info = sonarhandler.project_links.search_project_links(project_key)
	    for project_link_info in project_links_info:
	        link_name = project_link_info['name']
	        links_name.append(link_name)
	
	    if 'Gitlab Sources' not in links_name:
	        sonarhandler.project_links.create_project_links(project_key, 'Gitlab Sources',
	                                                        '{}/{}'.format(gitlab_url, path))
	        print('Create Gitlab link for {}'.format(project_key))
	
	    if 'Jenkins Job' not in links_name:
	        sonarhandler.project_links.create_project_links(project_key, 'Jenkins Job',
	                                                        '{}/job/{}'.format(jenkins_url, project_key))
	        print('Create Jenkins link for {}'.format(project_key))
	
	def sonarqube_user_operate_func(sonarhandler, username, gitlab_user_info, sonarqube_user_info):
	    """
	    处理用户数据
	    :param sonarhandler:
	    :param username:
	    :param gitlab_user_info:
	    :param sonarqube_user_info:
	    :return:
	    """
	    name = gitlab_user_info['name']
	    email = gitlab_user_info['email']
	
	    if username not in sonarhandler.users:
	        # 创建用户
	        sonarhandler.users.create_user(login=username, name=name, email=email,
	                                       password='{}@123'.format(username), local='true')
	        print('user {} create successful!'.format(username))
	
	    else:
	        # 更新用户数据
	        if name != sonarqube_user_info['name'] or email != sonarqube_user_info['email']:
	            sonarhandler.users.update_user(login=username, name=name, email=email)
	            print('update user {} information'.format(username))
	
	def sonarqube_group_operate_func(sonarhandler, gitlab_group_name, gitlab_group_members):
	    """
	    处理组数据
	    :param sonarhandler:
	    :param gitlab_group_name:
	    :param gitlab_group_members:
	    :return:
	    """
	    sonar_group_name = '{}-users'.format(gitlab_group_name)
	    if sonar_group_name not in sonarhandler.user_groups:
	        # 创建用户组
	        sonarhandler.user_groups.create_group(sonar_group_name)
	        print('group {} create successful!'.format(sonar_group_name))
	
	    sonar_group_users_info = sonarhandler.user_groups.get_users_belong_to_group(sonar_group_name)
	    sonar_group_users = [item['login'] for item in sonar_group_users_info]
	
	    need_add_users_to_sonar_user_group = list(set(gitlab_group_members) - set(sonar_group_users))
	    need_delete_users_from_sonar_user_group = list(set(sonar_group_users) - set(gitlab_group_members))
	
	    # 将用户添加到sonarqube用户组
	    for member in need_add_users_to_sonar_user_group:
	        if member in sonarhandler.users:
	            sonarhandler.user_groups.add_user_to_group(sonar_group_name, member)
	            print('add user {} to group {} successful'.format(member, sonar_group_name))
	
	    # 将用户从sonarqube用户组删除
	    for member in need_delete_users_from_sonar_user_group:
	        if member in sonarhandler.users:
	            sonarhandler.user_groups.delete_user_from_group(sonar_group_name, member)
	            print('delete user {} from group {} successful'.format(member, sonar_group_name))
	
	if __name__ == '__main__':
	    script_path = os.path.split(os.path.realpath(__file__))[0]
	    config = get_json_data(os.path.join(script_path, 'config', 'config.json'))
	    sonarqube_config = config['sonarqube_config']
	    gitlab_config = config['gitlab_config']
	
	    try:
	        sonarhandler = SonarAPIHandler(sonarqube_config['sonarqube_direct_url'],
	                                       sonarqube_config['sonar_user'],
	                                       sonarqube_config['sonar_password'])
	        print('{} connect successful!'.format(sonarhandler._sonarqube_url))
	    except Exception as err:
	        print("Connect {} Failed!".format(sonarhandler._sonarqube_url) + str(err))
	        sys.exit(1)
	
	    # 连接sonar的数据库
	    try:
	        db = pymysql.connect(**sonardb_config)
	        print("Open SonarQube Database Successful!")
	        cursor = db.cursor()
	    except Exception as err:
	        print("Failed to Open SonarQube Database!" + str(err))
	        sys.exit(1)
	
	    # 连接gitlab
	    try:
	        gl = gitlab.Gitlab(url=gitlab_config['gitlab_url'],
	                           email=gitlab_config['gitlab_email'],
	                           password=gitlab_config['gitlab_password'])
	        gl.auth()
	        print("Connect Gitlab Successful!")
	    except Exception as err:
	        print("Connect Gitlab Failed!" + str(err))
	        sys.exit(1)
	
	    # 生成sonarqube项目信息
	    sonarqube_projects_info = {item['key']: item for item in sonarhandler.projects}
	
	    # 获取sonarqube项目已存在的权限
	    permissions = ['codeviewer', 'user']
	    sonarqube_projects_exist_permissions = {}
	    for sonarqube_project_key in sonarqube_projects_info:
	        project_exist_permissions = {}
	        for permission in permissions:
	            groups = project_role_groups(cursor, sonarqube_project_key, permission)
	            users = project_role_users(cursor, sonarqube_project_key, permission)
	            project_exist_permissions[permission] = {'groups': groups, 'users': users}
	        sonarqube_projects_exist_permissions[sonarqube_project_key] = project_exist_permissions
	
	    # 关闭sonar数据库
	    db.close()
	    print('Close SonarQube Database.')
	
	    gs = gitlab_service(gl)
	
	    # 获取gitlab所有组成员
	    gitlab_groups_members = get_gitlab_groups_select_members(gs, state='active')
	
	    #获取gitlab所有项目成员
	    gitlab_projects_members = get_gitlab_projects_select_members(gs, state='active')
	
	    # 获取gitlab所有用户信息
	    gitlab_users_info = get_gitlab_users_info(gs)
	
	    # 获取sonarqube用户信息
	    sonarqube_users_info = {item['login']: item for item in sonarhandler.users}
	
	    # 生成sonarqube项目权限
	    sonarqube_projects_permissions = {}
	    for gitlab_project_path in gitlab_projects_members:
	        group = gitlab_project_path.split('/')[0]
	        project_key = gitlab_project_path.replace('/','-')
	        if project_key in sonarqube_projects_info:
	            sonarqube_projects_permissions[project_key]={'gitlab_project_path': gitlab_project_path,
	                                                         'group_name': group+'-users',
	                                                         'user_name': gitlab_projects_members[gitlab_project_path],
	                                                         'visibility': sonarqube_projects_info[project_key]['visibility'],
	                                                         'exist_permissions': sonarqube_projects_exist_permissions[project_key]}
	
	    # 处理用户数据
	    gitlab_usernames = list(gitlab_users_info.keys())
	    pool = multiprocessing.Pool(4)
	    for i in range(len(gitlab_usernames)):
	        pool.apply_async(sonarqube_user_operate_func, args=(sonarhandler, gitlab_usernames[i], gitlab_users_info[gitlab_usernames[i]], sonarqube_users_info[gitlab_usernames[i]],))
	    pool.close()
	    pool.join()
	
	    # 处理组数据
	    gitlab_groups = list(gitlab_groups_members.keys())
	    pool = multiprocessing.Pool(4)
	    for i in range(len(gitlab_groups)):
	        pool.apply_async(sonarqube_group_operate_func, args=(sonarhandler, gitlab_groups[i], gitlab_groups_members[gitlab_groups[i]], ))
	    pool.close()
	    pool.join()
	
	    # 对项目进行分组
	    sonarqube_projects_keys = list(sonarqube_projects_permissions.keys())
	    pool = multiprocessing.Pool(4)
	
	    for i in range(len(sonarqube_projects_keys)):
	        pool.apply_async(sonarqube_project_operate_func, args=(sonarhandler, sonarqube_projects_keys[i], sonarqube_projects_permissions[sonarqube_projects_keys[i]],))
	    pool.close()
	    pool.join()
