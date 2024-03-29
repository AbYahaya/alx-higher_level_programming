#!/usr/bin/python3
"""
Print error code gotten from a url usng requests
"""
from requests import get
import sys


if '__name__' == '__main__':
    url = sys.argv[1]
    response = get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print('Error code: {}'.format(response.status_code))
