#!/usr/bin/env python

import io
import os.path

from setuptools import setup, find_packages


def read_version(package):
    init_path = os.path.join(package, '__init__.py')
    with io.open(init_path, 'r') as fd:
        for line in fd:
            if line.startswith('__version__ = '):
                return line.split()[-1].strip().strip("'")


package_name = 'mocket'

setup(
    name=package_name,
    version=read_version(package_name),
    author='Giorgio Salluzzo',
    author_email='giorgio.salluzzo@gmail.com',
    url='https://github.com/mindflayer/python-mocket',
    description='Socket Mock Framework - for all kinds of socket animals, web-clients included - \
        with gevent/asyncio/SSL support',
    long_description=io.open('README.rst').read(),
    packages=find_packages(exclude=('tests', )),
    install_requires=[
        'python-magic',
        'six',
        'decorator',
        'hexdump',
        'urllib3',
    ],
    extras_require={
        'pook': ('pook>=0.2.1', )  # plugins version supporting mocket.plugins.pook.MocketEngine
    },
    test_suite='runtests.run_tests',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: BSD License',
    ],
)
