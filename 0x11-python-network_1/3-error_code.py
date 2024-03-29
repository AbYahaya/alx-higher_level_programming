#!/usr/bin/python3
"""
A pyton script to get a respons efrom a url and handle Http error
"""
from urllib.request import urlopen
from urllib.error import HttpError
import sys


if '__name__' == '__main__':
    url = sys.argv[1]
    with urlopen(url) as response:
        server_resp = response.read().decode('utf-8')
        print(server_resp)
    except HttpError as e:
        print('Error code:', e.code)
