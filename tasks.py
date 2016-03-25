#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from invoke import run, task
from invoke.util import log


@task
def clean():
    """clean - remove build artifacts."""
    run('rm -rf build/')
    run('rm -rf dist/')
    run('rm -rf pyrvt.egg-info')
    run('find . -name __pycache__ -delete')
    run('find . -name *.pyc -delete')
    run('find . -name *.pyo -delete')
    run('find . -name *~ -delete')

    log.info('cleaned up')


@task
def test():
    """test - run the test runner."""
    run('py.test --flake8 --cov-report html --cov pyrvt tests/', pty=True)
    run('open htmlcov/index.html')


@task
def lint():
    """lint - check style with flake8."""
    run('flake8 pyrvt tests')


@task(clean)
def publish():
    """publish - package and upload a release to the cheeseshop."""
    run('python setup.py sdist upload', pty=True)
    run('python setup.py bdist_wheel upload', pty=True)

    log.info('published new release')