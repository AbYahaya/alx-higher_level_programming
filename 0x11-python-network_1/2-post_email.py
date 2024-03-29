#!/usr/bin/python3
"""
Takes in an email and url and sends a post request to it then
prints the output decoded int utf-8
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys


if '__name__' == '__main__':
    url = sys.argv[1]
    email = {'email:': sys.argv[2]}
    email = urlencode(email)
    email = email.encode('ascii')
    request = Request(url, email)
    with urlopen(request) as response:
        returned_string = response.read().decode('utf-8')
        print(returned_string)
