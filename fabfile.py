from fabric.api import env, hosts, lcd, local, task
import fabric.contrib.project as project
import os

env.use_ssh_config = True

@task
def clean():
    """Clean up stale build files and tarballs"""
    with lcd(paths.local_workspace()):
        local('rm -rf build/*')
        local('rm -f *.tar.gz')
        local("find . -name '*.py[co]' | xargs rm")
