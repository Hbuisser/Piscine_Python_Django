#! /bin/sh

curl -s -I $1 | grep -i Location | cut -d " " -f2
