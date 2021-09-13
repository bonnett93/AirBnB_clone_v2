#!/usr/bin/python3
"""Module: 1-pack_web_static.py"""
from fabric.api import local
from datetime import date

def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    try:
        today = date.now()
        year = str(today.year)
        month = str(today.month)
        day = str(today.day)
        hour = str(today.hour)
        minute = str(today.minute)
        second = str(today.second)

        name = 'web_static_'+year+month+day+hour+minute+second+'.tgz'

        local('mkdir -p ./versions')
        local('tar -cvzf versions/{} ./web_static'.format(name))

        return 'versions/{}'.format(name)

    except:
        return None
