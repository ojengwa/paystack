# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path
from paystack.version import VERSION

here = path.abspath(path.dirname(__file__))
print(here)
# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='paystack',
    version=VERSION,
    description='A Paystack API wrapper in Python',
    long_description=long_description,
    url='https://github.com/ojengwa/paystack',
    download_url='https://github.com/ojengwa/paystack/tarball/' + VERSION,
    license='BSD',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',

    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests', 'site']),
    package_data={
        'paystack': [
            'data/paystack.crt',
            'data/paystack.key'
        ]
    },
    include_package_data=True,
    author='Bernard Ojengwa',
    install_requires=[
        'requests',
        'simplejson'
    ],
    author_email='bernardojengwa@gmail.com'
)
