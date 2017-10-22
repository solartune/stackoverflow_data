#!/bin/sh
kill -HUP `ps aux |grep gunicorn |grep config.wsgi |awk '{ print $2 }'`
