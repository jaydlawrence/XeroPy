#/usr/bin/env python
from setuptools import setup
import os

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name="XeroPy",
    description="Pythonic ORM implementation of the Xero API",
    zip_safe=False,
    version="1.3",
    packages=['XeroPy', ],
    install_requires=[
        'httplib2>=0.6.0',
        'oauth2==1.2.0',
        'SocksiPy-branch==1.02',
        'python-dateutil',
        #Jayd hack was not included but is needed
        #requires swig that must be installed using apt
        'M2Crypto'
    ]
)
