#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

NAME = 'wad'
DESCRIPTION = 'Dictionary class with advanced functionality'
URL = 'https://github.com/ShuYuHuang/what-a-dict'
EMAIL = 'b123767195@gmail.com'
AUTHOR = 'ShuYuHuang'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION
    
about = {}
project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
with open(os.path.join(here, project_slug, '__version__.py')) as f:
    exec(f.read(), about)

class UploadCommand(Command):
    description = 'Build and publish the package.'
    user_options = []
    
    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass
    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()

    
if __name__ == '__main__':
    setup(
        name=NAME,
        version=about['__version__'],
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/markdown',
        author=AUTHOR,
        author_email=EMAIL,
        python_requires=REQUIRES_PYTHON,
        url=URL,
        packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
        # If your package is a single module, use this instead of 'packages':
#         py_modules=['mypackage'],
        extras_require=EXTRAS,
        include_package_data=True,
        license='MIT',
        classifiers=[
            # Trove classifiers
            # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy'
        ],
        # $ setup.py publish support.
        cmdclass={
            'upload': UploadCommand,
        },
    )