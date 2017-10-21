#!/bin/sh
kill -HUP `ps aux |grep gunicorn |grep st.wsgi |awk '{ print $2 }'`
