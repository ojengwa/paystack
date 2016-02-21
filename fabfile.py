"""Summary."""

from fabric.api import local, task

from paystack.version import VERSION


@task
def install(version=""):
    """Install project artifacts.

    Args:
        version (str, optional): Description
    """
    local("pip install -r requirements.txt")
    local("pip install -r test-requirements.txt")


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
    build = local("python setup.py sdist")
    if build.succeeded:
        local("python setup.py sdist upload")


@task
def test():
    """Test project."""
    local(
        "coverage erase && nosetests  --with-coverage --cover-package=paystack/"
    )


@task
def tag(version=VERSION):
    """Deploy a version tag."""
    build = local("git tag {0}".format(version))
    if build.succeeded:
        local("git push --tags")
