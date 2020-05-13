import json
import urllib


def pretty_print_json(data):
    """
    :param data:
    :return:
    """
    return json.dumps(data, sort_keys=True, indent=4, encoding='utf-8', separators=(',', ':'))


def decode_json(data):
    """
    :param data:
    :return:
    """
    return json.JSONDecoder().decode(pretty_print_json(data))


def expand_url(url, params=None):
    """
    :param url:
    :param params:
    :return:
    """
    _url = url
    if params:
        _url += '?'
    paramFormat = '{}={}&'

    for key, value in params.items():
        if isinstance(value, list):
            for value2 in value:
                try:
                    _url += paramFormat.format(key, urllib.quote_plus(str(value2)))
                except:
                    _url += paramFormat.format(key, urllib.parse.quote_plus(str(value2)))
        else:
            try:
                _url += paramFormat.format(key, urllib.quote_plus(str(value)))
            except:
                _url += paramFormat.format(key, urllib.parse.quote_plus(str(value)))

    return _url


def get_paging_info(resp):
    """
    :param resp:
    :return:
    """
    msg = decode_json(resp.json())
    return msg['paging']['pageIndex'], msg['paging']['total'], msg['paging']['pageSize']


