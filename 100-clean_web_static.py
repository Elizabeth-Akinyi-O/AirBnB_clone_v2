#!/usr/bin/python3
"""
Deletes out-of-date archives, using the function do_clean.
Use: 'fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1' to execute. """

from fabric.api import *
import os
# Hosts the fabric will connect to
env.hosts = ['54.234.101.144', '54.89.28.233']


def do_clean(number=0):
    """Deletes out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives
    """
    number = 1 if int(number) == 0 else int(number)
# Get a list of files in the versions dir and sort them
    arch_list = sorted(os.listdir("versions"))
# Remove a specified no of files from the end of the list of archives
    [arch_list.pop() for i in range(number)]
# Change the local dir to versions and execute deletion
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in arch_list]

    with cd("/data/web_static/releases"):
        # List files in reverse order && split output
        arch_list = run("ls -tr").split()
        arch_list = [x for x in arch_list if "web_static_" in x]
        [arch_list.pop() for i in range(number)]
        [run("rm -rf ./{}".format(x)) for x in arch_list]   # Deletes
