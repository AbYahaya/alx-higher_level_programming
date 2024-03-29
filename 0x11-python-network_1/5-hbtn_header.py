#!/usr/bin/python3
"""
using requests package to get a specific response value from a url
"""
from requests import get
from sys import argv


if '__name__' == '__main__':
    url = argv[1]
    response = get(url)
    info = response.headers
    print(info.get('x-request-id'))
