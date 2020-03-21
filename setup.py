# Copyright (c) 2020 Xvezda <xvezda@naver.com>
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

from distutils.core import setup


import re
VERSION_FILE = '_version.py'
VERSION_REGEX = r'__version__ = ([\'"])([^\'"])+\1'
with open(VERSION_FILE, 'rt') as version_file:
    try:
        VERSION = re.search(VERSION_REGEX, version_file.read()).group(2)
    except IndexError:
        raise RuntimeError("version file '%s' cannot be found" % (VERSION_FILE,))


setup(name='maskprocessor',
      packages=['maskprocessor'],
      author='Xvezda',
      author_email='xvezda@naver.com',
      license='MIT',
      url='https://github.com/Xvezda/python-maskprocessor',
      keywords=['hash', 'hashcat', 'maskprocessor', 'bruteforce'],
      version=VERSION,
      description='Python maskprocessor implemenetation '
                  'inspired by hashcat maskprocessor',
      classifiers=[
          'Development Status :: 1 - Planning',
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
      })
