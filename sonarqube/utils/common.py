#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi


def strip_trailing_slash(url):
    """
    remove url's trailing slash

    :param url:
    :return:
    """
    if url.endswith('/'):
        url = url[:-1]
    return url

