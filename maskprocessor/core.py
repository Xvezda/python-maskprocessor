#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Xvezda <xvezda@naver.com>
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

from .__version__ import __version__

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
    """Expand mask characters."""
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
    """Mask processor generator.

    Built-in charsets:
        ?l = abcdefghijklmnopqrstuvwxyz
        ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
        ?d = 0123456789
        ?s = «space»!"#$%&'()*+,-./:;<=>?@[]^_`{|}~
        ?a = ?l?u?d?s
        ?b = 0x00 - 0xff

    Args:
        mask (str): String of mask characters.
        custom_charset1 (:obj:`str`, optional): First custom charsets.
        custom_charset2 (:obj:`str`, optional): Second custom charsets.
        custom_charset3 (:obj:`str`, optional): Third custom charsets.
        custom_charset4 (:obj:`str`, optional): Fourth custom charsets.

    Yields:
        str: Generated word.
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
            Word generator with a per-position configureable charset'''),
        epilog=dedent('''\
            Built-in charsets:
              ?l = abcdefghijklmnopqrstuvwxyz
              ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
              ?d = 0123456789
              ?s =  !"#$&'()*+,-./:;<=>?@[\]^_`{|}~
              ?a = ?l?u?d?s
              ?b = 0x00 - 0xff

            Examples:
              The following commands creates the following password candidates:
                * command: ?l?l?l?l?l?l?l?l
                  keyspace: aaaaaaaa - zzzzzzzz
                * command: -1 ?l?d ?1?1?1?1?1
                  keyspace: aaaaa - 99999
                * command: password?d
                  keyspace: password0 - password9
                * command: -1 ?l?u ?1?l?l?l?l?l19?d?d
                  keyspace: aaaaaa1900 - Zzzzzz1999
                * command: -1 ?dabcdef -2 ?l?u ?1?1?2?2?2?2?2
                  keyspace: 00aaaaa - ffZZZZZ
                * command: -1 efghijklmnop ?1?1?1
                  keyspace: eee - ppp

            For more information, check out following URLs.
                https://github.com/hashcat/maskprocessor#readme
                https://github.com/Xvezda/python-maskprocessor#readme'''))
    parser.add_argument('mask', type=str)
    parser.add_argument('-V', '--version',
                        help='show version information',
                        action='version',
                        version=__version__)
    custom_charset_group = parser.add_argument_group(
        title='custom charsets arguments',
        description='There are four commandline-parameters '
                    'to configure four custom charsets.\n'
                    'These commandline-parameters have four analogue '
                    'shortcuts called -1, -2, -3 and -4. '
                    'You can specify the chars directly on the command line.'
    )
    custom_charset_group.add_argument('--custom-charset1', '-1', type=str,
                                      metavar='CS')
    custom_charset_group.add_argument('--custom-charset2', '-2', type=str,
                                      metavar='CS')
    custom_charset_group.add_argument('--custom-charset3', '-3', type=str,
                                      metavar='CS')
    custom_charset_group.add_argument('--custom-charset4', '-4', type=str,
                                      metavar='CS')
    args = parser.parse_args()

    for i in maskprocessor(args.mask,
                           custom_charset1=args.custom_charset1,
                           custom_charset2=args.custom_charset2,
                           custom_charset3=args.custom_charset3,
                           custom_charset4=args.custom_charset4):
        print(i)


if __name__ == '__main__':
    main()

