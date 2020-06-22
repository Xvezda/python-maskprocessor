#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Xvezda <xvezda@naver.com>
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

from setuptools import setup, find_packages


with open('maskprocessor/__version__.py') as f:
    exec(f.read())


def readme():
    with open('README.md') as f:
        return f.read()


setup(name=__title__,
      author='Xvezda',
      author_email='xvezda@naver.com',
      license='MIT',
      url='https://github.com/Xvezda/python-maskprocessor',
      keywords=['hash', 'hashcat', 'maskprocessor', 'bruteforce'],
      version=__version__,
      packages=find_packages(),
      description='Python maskprocessor implementation '
                  'which inspired by hashcat maskprocessor',
      long_description_content_type='text/markdown',
      long_description=readme(),
      entry_points={
          'console_scripts': [
              'maskprocessor = maskprocessor.core:main',
          ]
      },
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Environment :: Console',
          'Topic :: Utilities',
          'Topic :: Security :: Cryptography',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
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
