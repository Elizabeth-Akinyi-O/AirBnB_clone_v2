#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack """

from fabric.api import *
from datetime import datetime


def do_pack():
    """ Generates an archive from the contents of the web_static folder """
# Generate a timestamp and format it into a string
    time = datetime.now()
# Create the versions directory
    new_archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
# Create a new archive
    create = local('tar -cvzf versions/{} web_static'.format(new_archive))
    if create is not None:
        return new_archive
    else:
        return None
