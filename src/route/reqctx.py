# coding: utf-8
"""
    reqctx.py
    `````````

    realize greenlet-local object for request environ storage

    :copyright: (c) 2016 by neo1218.
    :license: MIT, see LICENSE for more details.
"""

from werkzeug.wrappers import Request
from .hub import _request_ctx_hub
from contextlib import contextmanager


class PirateRequest(Request):
    """
    :class PirateRequest:
        the request object used by default in pirate.
        remembers the matched endpoint and views arguments.
    """
    def __init__(self, environ):
        super(PirateRequest, self).__init__(environ)
        self.endpoint = None
        self.views_args = None


@contextmanager
def requestcontext(app, environ):
    _request_ctx_hub.app = app
    _request_ctx_hub.url_adapter = app.url_map.bind_to_environ(environ)
    _request_ctx_hub.request = PirateRequest(environ)
    try:
        yield  _request_ctx_hub  # coroutine stack switch
    finally:
        _request_ctx_hub.request = None  # clean up
