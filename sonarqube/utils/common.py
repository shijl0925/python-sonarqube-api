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


def endpoint(url_pattern, method='GET', item=None):
    """

    :param url_pattern:
    :param method:
    :param item:
    :return:
    """
    def wrapped_func(f):
        def translate_params(*args, **kwargs):
            all_params = dict(get_default_kwargs(f))

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
            """

            :param self:
            :param args:
            :param kwargs:
            :return:
            """
            func_params = translate_params(*args, **kwargs)
            params = {}

            for key, value in func_params.items():
                if key in self.special_attributes_map:
                    params[self.special_attributes_map[key]] = value
                else:
                    params[key] = value

            response = None
            if method == 'GET':
                response = self._get(url_pattern, params=params)
            elif method == 'POST':
                response = self._post(url_pattern, params=params)

            if response:
                try:
                    if response.headers['Content-Type'] == 'application/json':
                        return response.json()
                    else:
                        return response.text
                except Exception as e:
                    return response.content

            if method == 'PAGE_GET':
                page_num = 1
                page_size = 1
                total = 2

                while page_num * page_size < total:
                    response = self._get(url_pattern, params=params).json()
                    if 'paging' in response:
                        page_num = response['paging']['pageIndex']
                        page_size = response['paging']['pageSize']
                        total = response['paging']['total']
                    else:
                        page_num = response['p']
                        page_size = response['ps']
                        total = response['total']

                    params['p'] = page_num + 1

                    for i in response[item]:
                        yield i

                    if page_num >= self.MAX_SEARCH_NUM:
                        break

        inner_func.__doc__ = f.__doc__
        return inner_func
    return wrapped_func


def GET(url_pattern):
    """

    :param url_pattern:
    :return:
    """
    return endpoint(url_pattern, method='GET')


def POST(url_pattern):
    """

    :param url_pattern:
    :return:
    """
    return endpoint(url_pattern, method='POST')


def PAGE_GET(url_pattern, item):
    """

    :param url_pattern:
    :param item:
    :return:
    """
    return endpoint(url_pattern, method='PAGE_GET', item=item)
