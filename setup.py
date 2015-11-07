from setuptools import setup, find_packages
import os
import re
import sys

#v = open(os.path.join(os.path.dirname(__file__), 'mako', '__init__.py'))
#VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
#v.close()

#readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

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
    #tests_require=['nose >= 0.11', 'mock'],
    #test_suite="nose.collector",
    zip_safe=False,
    install_requires=[
        'peppercorn',
        'markupsafe',
        'eor-htmlgen'
    ]
)
