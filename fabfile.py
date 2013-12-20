from fabric.api import env, hosts, lcd, local, task
import fabric.contrib.project as project
import os

import otto.web as web
from otto.util import paths

env.use_ssh_config = True
env['otto.web.build_dir'] = './build/staged'
env['otto.web.site'] = 'veselosky.me'
# For otto >= 0.3
env['otto.build_dir'] = 'build/staged'
env['otto.site'] = 'veselosky.me'
env['otto.home'] = '/home/vince/websites/'

@task
def B():
    """Set remote host to boadicea.octoped.net"""
    env.hosts.append('boadicea.octoped.net')

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = os.path.join(env['otto.build_dir'], 'htdocs')
DEPLOY_PATH = env.deploy_path

@task
def clean():
    """Clean up stale build files and tarballs"""
    with lcd(paths.local_workspace()):
        local('rm -rf build/*')
        local('rm -f *.tar.gz')
        local("find . -name '*.py[co]' | xargs rm")

@task
def build(relative=False):
    """Build the site (quick, changes only)"""
    target = env['otto.web.build_dir']
    with lcd(paths.local_workspace()):
        local('mkdir -p %s' % target)
        local('mkdir -p %s' % DEPLOY_PATH)
        local('cp -a etc %s/' % target)
        # Pelican is ignorant of statics outside the theme
        local('cp -a static/ %s' % DEPLOY_PATH)
        if relative:
            local('RELATIVE=1 pelican -s pelicanconf.py -o %s content' % DEPLOY_PATH)
        else:
            local('pelican -s pelicanconf.py -o %s content' % DEPLOY_PATH)

@task
def rebuild(relative=False):
    """Build the site from a clean slate"""
    clean()
    build(relative)

def regenerate():
    local('pelican -r -s pelicanconf.py')

@task
def serve():
    """Start a local server to serve the site for testing"""
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

@task
def reserve():
    """Build the site from a clean slate, then start the dev server"""
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

# pelican task, preserved for reference but I will use otto instead
# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
