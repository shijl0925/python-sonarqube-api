import json
import urllib

def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, indent=4, encoding='utf-8', separators=(',', ':'))

def decode_json(data):
    return json.JSONDecoder().decode(pretty_print_json(data))

def expand_url(url, params={}):
    _url = url
    if params:
        _url += '?'
    paramFormat = '{}={}&'

    for key, value in params.items():
        if isinstance(value, list):
            for value2 in value:
                _url += paramFormat.format(key, urllib.quote_plus(str(value2)))
        else:
            _url += paramFormat.format(key, urllib.quote_plus(str(value)))

    return _url

def get_paging_info(resp):
    msg = decode_json(resp.json())
    return msg['paging']['pageIndex'], msg['paging']['total'], msg['paging']['pageSize']


