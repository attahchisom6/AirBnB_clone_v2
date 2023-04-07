#!/usr/bin/python3
"""script to deploy decompressed files to my web servers
"""
from os import path
from fabric.api import run, env, put
from fabric.contrib import files

env.hosts = ['54.144.221.216', '54.209.215.95']


def do_deploy(archive_path):
    """deploy decompressed files"""
    if not path.exists(archive_path):
        return False

    temp = archive_path.split(".")[0]
    name = temp.split("/")[1]
    newPath = "/data/web_static/releases/" + name

    try:
        put(archive_path, "/tmp")
        run("mkdir -p {}".format(newPath))
        run("tar -xzf /tmp/{}.tgz -C {}".format(name, newPath))
        run("rm -rf /tmp/{}.tgz".format(name))
        run("mv {}/web_static/* {}/".format(newPath, newPath))
        run("rm -rf {}/web_static".format(newPath))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(newPath))
        return True
    except Exception:
        return False
