from setuptools import setup, find_packages
import os
import re
import sys


if sys.version_info < (3, 3):
    raise Exception("eor-forms requires Python 3.3 or higher.")

setup(name='eor-forms',
    version='1.0.0',
    description='A web form library for Pyramid and other Python web frameworks',
    long_description='',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
    license='MIT',
    packages=find_packages('.', exclude=['examples*', 'test*']),
    tests_require=['nose2'],
    test_suite="nose2.collector.collector",
    zip_safe=True,
    install_requires=[
        'peppercorn',
        'eor-htmlgen'
    ]
)
