#!/usr/bin/python3
"""
This will serve to clean up old files from our machine

Args:
    number of archives in our direcyory
"""
from fabric import local


def do_clean(number=0):
    """the directory versions and /data/web_static/releases must be
    searched for files to delete
    """
    if number == 0:
        int(number) = 2
    else:
        number += 1

    path = /data/web_static/releases/
    local("cd versions; ls -t | tail -n +{} | xargs rm -rf".format(number))
    local("cd {}; ls -t | tail -n +{} | xargs rm -rf".format(path, number))
