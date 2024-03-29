#!/usr/bin/python3
"""
Some usage of the urllib
"""
import urllib.request
import sys


if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print("X-Request-Id:", request_id)
        else:
            print("X-Request-Id not found in the response headers.")
except urllib.error.URLError as e:
    print("Error:", e.reason)
