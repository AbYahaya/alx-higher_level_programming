#!/bin/bash
#Takes in a url, and sends a get request with heare variable
curl -sX GET -H "X-School-User-Id:98" "$1"
