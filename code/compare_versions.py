#!/usr/bin/env python3

import argparse
import operator
import sys


class Version(tuple):
    def __new__(cls, version):
        v = tuple(int(_) for _ in version.split("."))
        return super(Version, cls).__new__(cls, v)

    def __str__(self):
        return ".".join(str(_) for _ in self)

    @staticmethod
    def cmp(v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="""Compare version numbers.

    When no comparison operator is provided comparison result is displayed.
    When comparison operator is provided exit code represents comparison result.

    Return values, when no operator provided:
        -1 when v1 < v2
         0 when v1 == v2
         1 when v1 > v2

    Exit codes, when operator provided:
        0 when operator(v1, v2) == True
        1 when operator(v1, v2) == False
    """)
parser.add_argument('version', nargs=2, help='Version number, e.g. 1.0.0')
parser.add_argument('--operator', action="store", help='Comparison operator to use, e.g. lt, eq, gt')
parser.add_argument('--verbose', action="store_true", default=False, help='Be verbose, describe comparison details')
args = parser.parse_args()

try:
    v1 = Version(args.version[0])
    v2 = Version(args.version[1])
    if args.operator:
        op = getattr(operator, args.operator)

except (AttributeError, ValueError) as _:
    parser.print_help()
    exit(1)

if not args.operator:
    r = Version.cmp(v1, v2)
    if args.verbose:
        print("Comparing version numbers {} and {}, result: {}".format(v1, v2, r))
    else:
        print(r)
else:
    r = op(v1, v2)
    if args.verbose:
        print("{} {} {} {}".format(v1, op.__name__, v2, r))
    exit(not r)
