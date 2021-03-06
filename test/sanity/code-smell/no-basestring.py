#!/usr/bin/env python

import os
import re
import sys


def main():
    skip = set([
        'test/sanity/code-smell/%s' % os.path.basename(__file__),
        'lib/ansible/module_utils/six/__init__.py',
    ])

    for path in sys.argv[1:]:
        if path in skip:
            continue

        with open(path, 'r') as path_fd:
            for line, text in enumerate(path_fd.readlines()):
                match = re.search(r'(isinstance.*basestring)', text)

                if match:
                    print('%s:%d:%d: do not use `isinstance(s, basestring)`' % (
                        path, line + 1, match.start(1) + 1))


if __name__ == '__main__':
    main()
