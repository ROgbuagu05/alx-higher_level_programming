#!/bin/bash
# Make request and display response body size in bytes
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
