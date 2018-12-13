#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

class jenkins_service(object):
    def __init__(self, jenkins_server):
        self.jenkins_server = jenkins_server

    def create_new_view(self, view_name):
        """
        创建View
        :param view_name:
        :return:
        """
        template_view_config = self.jenkins_server.get_view_config('template')
        view_config = template_view_config.replace('template',view_name)
        self.jenkins_server.create_view(view_name, view_config)

    def create_new_job(self, job_name, project_type, git_url):
        """
        创建新的job
        :param job_name:
        :param project_type:
        :param git_url:
        :return:
        """
        if project_type == 'java':
            jenkins_template = 'template-java'
        elif project_type == 'android':
            jenkins_template = 'template-android'
        elif project_type == 'js':
            jenkins_template = 'template-js'
        elif project_type == 'ts':
            jenkins_template = 'template-ts'
        elif project_type == 'ios':
            jenkins_template = 'template-ios'
        elif project_type == 'python':
            jenkins_template = 'template-python'

        template_config = self.jenkins_server.get_job_config(jenkins_template)
        job_config = template_config.replace('template',git_url).replace('job_name',job_name)
        self.jenkins_server.create_job(job_name, job_config)

    def reconfig_exist_job(self, job_name, project_type, git_url):
        """
        重置已存在的job
        :param job_name:
        :param project_type:
        :param git_url:
        :return:
        """
        if project_type == 'java':
            jenkins_template = 'template-java'
        elif project_type == 'android':
            jenkins_template = 'template-android'
        elif project_type == 'js':
            jenkins_template = 'template-js'
        elif project_type == 'ts':
            jenkins_template = 'template-ts'
        elif project_type == 'ios':
            jenkins_template = 'template-ios'
        elif project_type == 'python':
            jenkins_template = 'template-python'

        template_config= self.jenkins_server.get_job_config(jenkins_template)
        job_config = template_config.replace('template',git_url).replace('job_name',job_name)
        self.jenkins_server.reconfig_job(job_name, job_config)

    def set_job_status(self, job_name, job_status):
        """
        设置job的状态
        :param job_name:
        :param job_status:
        :return:
        """
        if job_status == "enabled":
            self.jenkins_server.enable_job(job_name)
        elif job_status == "disabled":
            self.jenkins_server.disable_job(job_name)

    def get_running_jobs(self):
        """
        获取正在运行的job
        :return:
        """
        running_jobs = []
        for i in self.jenkins_server.get_running_builds():
            running_jobs.append(i['name'])
        return running_jobs

    def job_build_status(self, job_name):
        """
        获取job的状态
        :param job_name:
        :return:
        """
        return self.jenkins_server.get_job_info(job_name)['buildable']

    def job_build_branch(self, job_name, build_number):
        """
        获取编译job的分支
        :param job_name:
        :param build_number:
        :return:
        """
        build_info = self.jenkins_server.get_build_info(job_name, build_number)
        _actions = [x for x in build_info['actions'] if x and "lastBuiltRevision" in x]
        build_branch = _actions[0]["lastBuiltRevision"]["branch"][0]["name"].split('/')[1]
        return build_branch

    def get_jobs_name(self):
        """
        获取jenkins所有的项目名称
        :return:
        """
        jobs = self.get_jobs()
        all_job_names = [j['name'] for j in jobs]
        return all_job_names

    def get_lastbuild_failed_jobs(self, interval):
        """
        获取jenkins报错项目
        :param interval: 时间间隔
        :return:
        """
        now_timestamp = int(time.time())
        jobs_lastbuild_result = []
        for job_name in self.get_jobs_name():
            job_info = self.get_job_info(job_name)

            build_nums = [j['number'] for j in job_info['builds']]
            last_one_build_number = job_info['nextBuildNumber'] - 1
            last_but_one_build_number = job_info['nextBuildNumber'] - 2

            if job_info['nextBuildNumber'] > 1 and last_one_build_number in build_nums and last_but_one_build_number in build_nums:
                last_build_info = self.get_build_info(job_name,last_one_build_number)
                last_but_one_build_info = self.get_build_info(job_name,last_but_one_build_number)

                last_build_result = last_build_info['result']
                last_but_one_build_result = last_but_one_build_info['result']
                last_build_time = int(last_build_info['timestamp']) / 1000
                interval_time = now_timestamp - last_build_time
                if last_build_result == 'FAILURE' and last_but_one_build_result != 'FAILURE' and interval_time < 60 * interval:
                    jobs_lastbuild_result.append(job_name)
        return jobs_lastbuild_result
