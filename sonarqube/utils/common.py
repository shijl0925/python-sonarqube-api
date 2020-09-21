#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import inspect


def strip_trailing_slash(url):
    """
    remove url's trailing slash

    :param url:
    :return:
    """
    if url.endswith('/'):
        url = url[:-1]
    return url


def get_args(func):
    """
    Returns a sequence of list (args) for func
    :param func:
    :return:
    """
    argspec = inspect.getargspec(func)

    if not argspec.defaults:
        args = argspec.args[1:]
    else:
        args = argspec.args[1:-len(argspec.defaults)]

    return args


def get_default_kwargs(func):
    """
    Returns a sequence of tuples (kwarg_name, default_value) for func

    :param func:
    :return:
    """
    argspec = inspect.getargspec(func)

    if not argspec.defaults:
        return []

    return zip(argspec.args[-len(argspec.defaults):], argspec.defaults)


def endpoint(url_pattern, method='GET'):
    def wrapped_func(f):
        def translate_params(*args, **kwargs):
            # print("args: {}".format(args))
            # print("kwargs: {}".format(kwargs))

            all_params = dict(get_default_kwargs(f))
            # print("all_params: {}".format(all_params))
            # print("get_args(f): {}".format(get_args(f)))

            if len(get_args(f)) < len(args):
                additional_values = args[len(get_args(f)):]
                func_parameters = inspect.getargspec(f).args[1:]
                additional_args = func_parameters[len(get_args(f)):len(get_args(f))+len(additional_values)]
                all_params.update(dict(zip(additional_args, additional_values)))

            all_params.update(dict(zip(get_args(f), args)))
            all_params.update(kwargs)

            for key in list(all_params.keys()):
                if not all_params[key]:
                    del all_params[key]

            return all_params

        def inner_func(self, *args, **kwargs):
            func_params = translate_params(*args, **kwargs)
            params = {}

            for key, value in func_params.items():
                if key in self.special_attributes_map:
                    params[self.special_attributes_map[key]] = value
                else:
                    params[key] = value

            # print(params)

            if method == 'GET':
                response = self.get(url_pattern, params=params)
            elif method == 'POST':
                response = self.post(url_pattern, params=params)
            else:
                response = None
            try:
                if response.headers['Content-Type'] == 'application/json':
                    return response.json()
                else:
                    return response.text
            except Exception as e:
                return response.content

        inner_func.__doc__ = f.__doc__
        return inner_func
    return wrapped_func


def GET(url_pattern):
    return endpoint(url_pattern, method='GET')


def POST(url_pattern):
    return endpoint(url_pattern, method='POST')
