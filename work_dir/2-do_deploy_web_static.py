#!/usr/bin/python3
"""
script to deploy decompresses files to my servers
"""
from os import path
from fabric.api import run, env, put

env.hosts = ["54.144.221.216", "54.209.215.95"]
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    a function to deploy data to our servers
    """
    if not path.exists("archive_path"):
        return False

    temp = archive_path.split(".")[0]
    name = temp.split('/')[1]
    newPath = "/data/web_static/releases/" + name

    try:
        put(archive_path, "/tmp")
        run(mkdir -p newPath)
        run(tar -xzf name.tgz -C
