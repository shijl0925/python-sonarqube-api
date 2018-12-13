#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import logging
import os
import datetime
import time
import functools

#今天的日期
today = datetime.datetime.now().strftime('%Y-%m-%d')

#当前时间
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_json_data(file_name):
    """
    获取json文件数据
    :param file_name:
    :return:
    """
    with open(file_name,"r") as f:
        data = json.load(f)
    return data

def update_json_data(file_name, dict_data):
    """
    将数据写入json文件
    :param file_name:
    :param dict_data:
    :return:
    """
    with open(file_name, 'w') as f:
        f.write(json.dumps(dict_data, sort_keys=True, indent = 4, encoding='utf-8', ensure_ascii=True))

def get_template(template_filename):
    """
    获取模板
    :param template_filename:
    :return:
    """
    with open(template_filename, 'r') as templatefile:
        template = templatefile.read()
    return template

def search_str_in_file(file, search_str):
    """
    搜索字符串在文件中的行数
    :param file:
    :param str:
    :return:
    """
    for index, line in enumerate(open(file, 'r')):
        if search_str in line:
            line_num = index
    return line_num

def judge_day(start_day, end_day):
    """
    计算两个日期之间的差异天数
    :param start_day:
    :param end_day:
    :return:
    """
    start_sec = time.mktime(time.strptime(start_day,"%Y-%m-%d"))
    end_sec = time.mktime(time.strptime(end_day,"%Y-%m-%d"))

    work_days = int((end_sec - start_sec)/(24*60*60))
    return work_days

def clock(func):
    """
    装饰器，用于计算函数执行时间
    :param func:
    :return:
    """
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' %(k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s)' % (elapsed, func.__name__, arg_str))
        return result
    return clocked

class Logger(object):
    def __init__(self):
        pass

    def create_logger(self,name,file):
        logger = logging.getLogger(name)
        logger.setLevel(level = logging.INFO)
        handler = logging.FileHandler("{}.log".format(os.path.splitext(os.path.realpath(file))[0]),mode='a')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)

        logger.addHandler(handler)
        logger.addHandler(console)
        return logger
