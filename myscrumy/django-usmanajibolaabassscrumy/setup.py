import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

#allow setup to run from any paths

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
name = 'django-usmanajibolaabassscrumy',
version = '1.0',
packages = find_packages(),
license = 'BSD license',
author = 'Usman Abass'
)
