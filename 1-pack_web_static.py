#!/usr/bin/python3
"""
A fabric script that generates a tgz archieve from all in the web_static directory
"""
from fabric import local
from datetime import datetime
from os import path

def do_pack():
    """pack desired files into a comprrssed form
    """
    path.exists("versions") is False:
        local("mkdir versions")

    try:
        now = datetime.now()
        formatt = "%Y%m%d%H%M%S"
        archieve_path = "versions/web_static_{}.tgz".format(now.strftime(formatt))
        local("tar -cfvz {} web_static".format(archieve_path)
        return (archieve_path)
    except Exception:
        return (None)
