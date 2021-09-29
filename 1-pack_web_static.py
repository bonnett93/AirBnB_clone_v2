#!/usr/bin/python3
"""Module: 1-pack_web_static.py"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""

    local('mkdir -p ./versions')
    today = datetime.now()
    print(today)
    year = str(today.year)
    month = str(today.month)
    day = str(today.day)
    hour = str(today.hour)
    minute = str(today.minute)
    second = str(today.second)
    name = 'web_static_'+year+month+day+hour+minute+second+'.tgz'

    try:
        local('tar -cvzf versions/{} ./web_static'.format(name))
        return 'versions/{}'.format(name)

    except:
        return None
