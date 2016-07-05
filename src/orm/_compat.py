# coding: utf-8
"""
    pirate-orm_compat
    `````````````````

    internal python 2.x/3.x compatibility layer
"""

import sys


PY2 = sys.version_info[0] == 2


if PY2:
    def iteritems(d):
        return d.iteritems()

    def itervalues(d):
        return d.itervalues()

    xrange = xrange

    string_types = (unicode, bytes)

else:
    def iteritems(d):
        return iter(d.items())

    def itervalues(d):
        return iter(d.values())

    xrange = range

    string_types(str,)
