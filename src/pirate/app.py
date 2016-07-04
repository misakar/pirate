# coding: utf-8
"""
    app.py
    ``````

    pirate wsgi app

    :copyright: (c) 2016 by neo1218.
    :license: MIT, see LICENSE for more details.
"""

import json
import functools
from werkzeug.routing import Map
from werkzeug.exceptions import HTTPException
from src.route.resp import PirateResponse
from src.route.reqctx import PirateRequest, requestcontext
from src.route.hub import _request_ctx_hub, request
from gevent import monkey
monkey.patch_all()


class Pirate(object):
    """
    :class Pirate:
        the pirate object implements a WSGI application and acts as
        the central object
    """
    request_class = PirateRequest

    response_class = PirateResponse

    secret_key = None

    def __init__(self):
        self.debug = False
        self.route_functions = {}  # store route function
        self.error_handlers = {}
        self.url_map = Map()  # url map rules

    def errorhandler(self, code):
        def decorator(f):
            self.error_handlers[code] = f
            return f
        return decorator

    def match_request(self):
        rv = _request_ctx_hub.url_adapter.match()
        request.endpoint, request.views_args = rv
        return rv

    def dispatch_request(self):
        try:
            endpoint, values = self.match_request()
            return self.route_functions[endpoint](**values)
        except HTTPException, e:
            handler = self.error_handlers.get(e.code)
            if handler is None:
                return e
            return handler(e)
        except Exception, e:
            handler = self.error_handlers.get(500)
            if self.debug or handler is None:
                raise
            return handler(e)

    def make_response(self, rv):
        if isinstance(rv, self.response_class):
            return rv
        if isinstance(rv, basestring):
            return self.response_class(rv)
        if isinstance(rv, tuple):
            return self.response_class(*rv)  # unpack rv tuple
        return self.response_class.force_type(rv, request.environ)

    def firing(self, host='localhost', port=8090, **options):
        # run pirate app on gevent wsgiserver
        from gevent.wsgi import WSGIServer
        if 'debug' in options:
            self.debug = options.pop('debug')
            if self.debug:
                from werkzeug.debug import DebuggedApplication
                app = DebuggedApplication(self, evalex=True)
            else:
                app = self
        WSGIServer((host, port), app).serve_forever()

    def wsgi_app(self, environ, start_response):
        # actual wsgi application.
        with requestcontext(self, environ):
            # _request_ctx_hub
            rv = self.dispatch_request()
            resp = self.make_response(rv)
            return resp(environ, start_response)

    def __call__(self, environ, start_response):
        # call for wsgi app
        return self.wsgi_app(environ, start_response)

    def tojson(self, f):
        @functools.wraps(f)
        def decorator(*args, **kwargs):
            rv = f(*args, **kwargs)
            headers = None
            if isinstance(rv, tuple):
                # have headers
                rv, headers = rv
            rv = json.dumps(rv, indent=1, ensure_ascii=False)
            rv = self.make_response(rv)
            if headers:
                rv.headers.extend(headers)
            return rv
        return decorator
