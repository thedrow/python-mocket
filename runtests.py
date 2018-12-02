#!/usr/bin/env python

import sys

import pytest


def run_tests(args=None, python35=False):
    args = args or []

    major, minor = sys.version_info[:2]

    # aiohttp available on Python > 3.4
    if major == 3 and minor > 4:
        python35 = True

    if not any(a for a in args[1:] if not a.startswith('-')):
        args.append('tests/main')
        args.append('mocket')
        args.append('tests/tests27')

        if python35:
            args.append('tests/tests35')

    sys.exit(pytest.main(args))


if __name__ == '__main__':
    run_tests(sys.argv)
