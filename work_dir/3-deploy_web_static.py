#!/usr/bin/python3
"""
The Main purpose of this script will be to call functions that deploy
contents to our web servers
"""
from os import path
from fabric.api import env, local, put, run
from datetime import datetime

env.hosts = ['54.144.221.216', '54.209.215.95']
env.user = "ubuntu"


def do_pack():
    """
    returns the path to our archive files
    """
    try:
        if not path.exists("versions"):
            local("mkdir versions")

        now = datetime.now()
        formatt = "%Y%m%d%H%M%S"
        archiveName = "web_static_{}.tgz".format(now.strftime(formatt))
        archive_path = "/versions/{}".format(archiveName)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None

    def do_deploy(archive_path):
        """
        deploy decompressed files to my servers
        return true on success, false on failue
        """
        if not path.exists(archive_path):
            return False

        temp = archive_path.split('.')[0]
        file = temp.split('/')[1]
        folder = "/data/web_static/releases/" + file

        try:
            put(archive_path, "/tmp/")
            run("mkdir -p {}".format(folder))
            run("tar -xzf /tmp/{}.tgz -C {}".format(file, folder))
            run("rm -rf /tmp/{}.tgz".format(file))
            run("mv {}/web_static/* {}".format(folder, folder))
            run("rm -r {}/web_static".format(folder))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_stayic/current".format(folder))
            return True
        except Exception:
            return False

    def deploy():
        """
        distribute data to my servers
        """
        try:
            archive = do_pack()
        except Exception:
            return False
        do_deploy(archive)
