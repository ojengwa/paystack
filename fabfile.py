"""Summary."""
import re

from fabric.api import local, task

from setup import VERSION

_version_re = re.compile(r'__version__\s+=\s+(.*)')


@task
def install(version=""):
    """Install project artifacts.

    Args:
        version (str, optional): Description
    """
    local("pip install -r requirements.txt")
    local("python setup.py install")


@task
def clean():
    """Remove all the .pyc files."""
    local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)
    # Remove the dist folder
    local("rm -rf ./dist && rm -rf paystack.egg-info")


@task
def push(msg):
    """Push to github.

    Args:
        msg (str, required): Description
    """
    clean()
    local("git add . && git commit -m '{}'".format(msg))
    local("git push")


@task
def publish():
    """Deploy the app to PYPI.

    Args:
        msg (str, optional): Description
    """
    clean()
    local("python setup.py bdist_egg")
    build = local("python setup.py sdist")
    if build.succeeded:
        upload = local("python setup.py sdist upload")
        if upload.succeeded:
            clean()


@task
def test():
    """Test project."""
    local(
        "coverage erase && nosetests  --with-coverage --cover-package=paystack"
    )


@task
def tag(tag=VERSION):
    """Deploy a version tag."""
    build = local("git tag {0}".format(tag))
    if build.succeeded:
        local("git push --tags")
