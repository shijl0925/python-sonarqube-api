#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import inspect
from functools import wraps


def strip_trailing_slash(url):
    """
    remove url's trailing slash

    :param url:
    :return:
    """
    if url.endswith("/"):
        url = url[:-1]
    return url


def arg_spec_factory(f, *args, **kwargs):
    """

    :param f:
    :param args:
    :param kwargs:
    :return:
    """
    if not callable(f):
        raise ValueError("Expected a callable object")

    # 获取函数参数的详细信息
    arg_spec = inspect.getfullargspec(f)

    # 初始化参数字典
    params = {}

    # 处理关键字参数和默认参数
    if arg_spec.defaults:
        num_defaults = len(arg_spec.defaults)
        for name, default in zip(arg_spec.args[-num_defaults:], arg_spec.defaults):
            params[name] = default

    # 处理位置参数
    positional_args = arg_spec.args[1: -len(arg_spec.defaults)] if args else arg_spec.args[1:]
    length = len(positional_args)
    if length < len(args):
        additional_values = args[length:]
        additional_args = arg_spec.args[
            length + 1: length + len(additional_values) + 1
        ]
        params.update(dict(zip(additional_args, additional_values)))

    params.update(dict(zip(positional_args, args)))

    # 更新关键字参数
    params.update(kwargs)

    # 确保所有参数都是有效的，即在函数定义中存在
    valid_params = arg_spec.args
    if arg_spec.varargs:
        valid_params += [arg_spec.varargs]
    if arg_spec.varkw:
        valid_params += [arg_spec.varkw]

    # 删除多余参数
    filtered_params = {key: value for key, value in params.items() if value is not None and key in valid_params}

    return filtered_params


def endpoint(url_pattern, method="GET", filters=None):
    """

    :param url_pattern:
    :param method:
    :param filters:
    :return:
    """

    def wrapped_func(f):
        @wraps(f)
        def inner_func(self, *args, **kwargs):  # pylint: disable=inconsistent-return-statements
            """

            :param self:
            :param args:
            :param kwargs:
            :return:
            """
            params = arg_spec_factory(f, *args, **kwargs)
            if filters is not None:
                for key in filters:
                    if key in params:
                        params[filters[key]] = params.pop(key)

            response = None
            if method == "GET":
                response = self._get(url_pattern, params=params)  # pylint: disable=protected-access
            elif method == "POST":
                response = self._post(url_pattern, data=params)  # pylint: disable=protected-access

            if not response:
                return

            try:
                if response.headers["Content-Type"] == "application/json":
                    return response.json()
                else:
                    return response.text
            except Exception:  # pylint: disable=broad-exception-caught
                return response.content

        return inner_func

    return wrapped_func


def GET(url_pattern, filters=None):
    """

    :param url_pattern:
    :param filters:
    :return:
    """
    return endpoint(url_pattern, method="GET", filters=filters)


def POST(url_pattern, filters=None):
    """

    :param url_pattern:
    :param filters:
    :return:
    """
    return endpoint(url_pattern, method="POST", filters=filters)
