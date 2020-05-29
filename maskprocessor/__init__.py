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


# Generate charsets
charset_l = string.ascii_lowercase
charset_u = string.ascii_uppercase
charset_d = string.digits
charset_s = ' ' + string.punctuation
charset_a = charset_l + charset_u + charset_d + charset_s
charset_b = ''.join([chr(v) for v in range(0x00, 0xff+1)])

# Custom charsets
charset_1 = ''
charset_2 = ''
charset_3 = ''
charset_4 = ''


def expand(mask):
    if not mask:
        return []
    charsets = []
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
            elif c2 == '1':
                charsets += [charset_1]
            elif c2 == '2':
                charsets += [charset_2]
            elif c2 == '3':
                charsets += [charset_3]
            elif c2 == '4':
                charsets += [charset_4]
            elif c2 == '?':
                charsets += ['?']
            else:
                raise SyntaxError("invalid character '%s'" % (c2,))
        else:
            charsets += [c]
    return charsets


def maskprocessor(mask,
                  custom_charset1=None,
                  custom_charset2=None,
                  custom_charset3=None,
                  custom_charset4=None):
    """Mask processor generator

    Built-in charsets:
        ?l = abcdefghijklmnopqrstuvwxyz
        ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
        ?d = 0123456789
        ?s = «space»!"#$%&'()*+,-./:;<=>?@[]^_`{|}~
        ?a = ?l?u?d?s
        ?b = 0x00 - 0xff
    """
    charsets = []

    global charset_1, charset_2, charset_3, charset_4

    charset_1 = ''.join(expand(custom_charset1))
    charset_2 = ''.join(expand(custom_charset2))
    charset_3 = ''.join(expand(custom_charset3))
    charset_4 = ''.join(expand(custom_charset4))

    charsets = expand(mask)

    for result in product(*charsets):
        yield ''.join(result)


def main():
    import argparse
    from textwrap import dedent
    parser = argparse.ArgumentParser(
        'maskprocessor',
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
    # There are four commandline-parameters to configure four custom charsets.
    parser.add_argument('--custom-charset1', '-1', type=str)
    parser.add_argument('--custom-charset2', '-2', type=str)
    parser.add_argument('--custom-charset3', '-3', type=str)
    parser.add_argument('--custom-charset4', '-4', type=str)
    args = parser.parse_args()

    for i in maskprocessor(args.mask,
                           custom_charset1=args.custom_charset1,
                           custom_charset2=args.custom_charset2,
                           custom_charset3=args.custom_charset3,
                           custom_charset4=args.custom_charset4):
        print(i)


if __name__ == '__main__':
    main()


# vim:set shiftwidth=4 softtabstop=4 expandtab
