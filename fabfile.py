"""fabfile to deploy the static files of django-introduction on your server.
"""
from fabric.api import *
from fabric.contrib import console, files
from fabric.utils import abort, fastprint


ERRMSG = """No remotepath specified.

Please specify a remote path where the static files will be deployed:

    $ fab deploy:/path/where/static/files/go

It's also possible to specify remotepath in a fabricrc file:

    remotepath = /path/where/static/files/go
"""


def deploy(remotepath=None):
    """Deploys the static files on a remote server."""
    if not remotepath:
        remotepath = env.get('remotepath')
    if not remotepath:
        abort(ERRMSG)
    local('make clean static')
    question = 'Continue and deploy static files '
    question += 'to %(host_string)s:%(remotepath)s?' % env
    if not console.confirm(question):
        abort('Deployment cancelled.')
    if files.exists(remotepath):
        run('rm -rf %s' % remotepath)
    run('mkdir %s' % remotepath)
    put('static/*', remotepath)
    put('static/.htaccess', remotepath)
    msg = 'Successfully deployed static files '
    msg += 'to %(host_string)s:%(remotepath)s.' % env
    fastprint(msg)
