#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept
curl -sI ALLOW $1 -L | grep "Allow" | cut -f2- -d' '
