"""
This stub allows the user to fallback to their system installation of
praw if the bundled package is missing. This technique was inspired by the
requests library and how it handles dependencies.

Reference:
    https://github.com/kennethreitz/requests/blob/master/requests/packages/__init__.py
"""
from __future__ import absolute_import
import sys


__praw_hash__ = 'ad0dbcf49d5937ffd39e13e45ebcb404b00c582a'
__praw_bundled__ = True


try:
    from . import praw
except ImportError:
    import praw
    if not praw.__version__.startswith('3.'):
        raise RuntimeError('Invalid PRAW version ({0}) detected, '
                           'rtv requires PRAW version 3'.format(praw.__version__))
    sys.modules['%s.praw' % __name__] = praw
    __praw_bundled__ = False
