#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Xvezda <xvezda@naver.com>
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

from setuptools import setup


import re
VERSION_FILE = 'maskprocessor/_version.py'
VERSION_REGEX = r'__version__ = ([\'"])([^\'"]+)\1'
with open(VERSION_FILE, 'rt') as version_file:
    try:
        VERSION = re.search(VERSION_REGEX, version_file.read()).group(2)
    except IndexError:
        raise RuntimeError("version file '%s' cannot be found" % (VERSION_FILE,))


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='maskprocessor',
      author='Xvezda',
      author_email='xvezda@naver.com',
      license='MIT',
      url='https://github.com/Xvezda/python-maskprocessor',
      keywords=['hash', 'hashcat', 'maskprocessor', 'bruteforce'],
      version=VERSION,
      packages=['maskprocessor'],
      description='Python maskprocessor implemenetation '
                  'which inspired by hashcat maskprocessor',
      long_description_content_type='text/markdown',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Topic :: Utilities',
          'Topic :: Security :: Cryptography',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      project_urls={
        'Repository': 'https://github.com/Xvezda/python-maskprocessor',
        'Bug Reports': 'https://github.com/Xvezda/python-maskprocessor/issues',
      },
      zip_safe=False)
