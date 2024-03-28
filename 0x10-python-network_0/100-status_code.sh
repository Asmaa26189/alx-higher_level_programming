#!/bin/bash
# bash script
curl -L -s -X HEAD -w "%{http_code}" "$1"
