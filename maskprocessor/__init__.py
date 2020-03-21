#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Xvezda <xvezda@naver.com>
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ._version import __version__

import sys
import string
from itertools import product


def gen_charset(start, end):
    return ''.join([chr(v) for v in range(start, end+1)])


def maskprocessor(mask):
    """Mask processor generator

    ?l = abcdefghijklmnopqrstuvwxyz
    ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ?d = 0123456789
    ?s = «space»!"#$%&'()*+,-./:;<=>?@[]^_`{|}~
    ?a = ?l?u?d?s
    ?b = 0x00 - 0xff
    """
    charsets = []
    # Generate charsets
    charset_l = string.ascii_lowercase
    charset_u = string.ascii_uppercase
    charset_d = string.digits
    charset_s = ' ' + string.punctuation
    charset_a = charset_l + charset_u + charset_d + charset_s
    charset_b = gen_charset(0x00, 0xff)

    # Parse mask
    it = iter(mask)
    while True:
        try:
            c = next(it)
        except StopIteration:
            break
        if c == '?':
            try:
                c2 = next(it)
            except StopIteration:
                break
            if c2 == 'l':
                charsets += [charset_l]
            elif c2 == 'u':
                charsets += [charset_u]
            elif c2 == 'd':
                charsets += [charset_d]
            elif c2 == 's':
                charsets += [charset_s]
            elif c2 == 'a':
                charsets += [charset_a]
            elif c2 == 'b':
                charsets += [charset_b]
            elif c2 == '?':
                charsets += ['?']
            else:
                raise SyntaxError("invalid character '%s'" % (c2,))
        else:
            charsets += [c]

    for result in product(*charsets):
        yield ''.join(result)


if __name__ == '__main__':
    import argparse
    from textwrap import dedent
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=dedent('''\
            word generator with a per-position configureable charset'''),
        epilog=dedent('''\
            built-in charsets:
              ?l = abcdefghijklmnopqrstuvwxyz
              ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
              ?d = 0123456789
              ?s =  !"#$&'()*+,-./:;<=>?@[\]^_`{|}~
              ?a = ?l?u?d?s
              ?b = 0x00 - 0xff'''))
    parser.add_argument('mask', type=str)
    parser.add_argument('-V', '--version',
                        help='show version information',
                        action='version',
                        version=__version__)
    args = parser.parse_args()

    for i in maskprocessor(args.mask):
        print(i)


# vim:set shiftwidth=4 softtabstop=4 expandtab
