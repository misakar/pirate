# coding: utf-8
"""
    route.py
    ````````

    the core module for pirate-route system.
    provide a greenlet decorator :route:
    for:
        match and dispatch request;
        generate and return response;
        make route function as coroutine.

    :copyright: (c) 2016 by neo1218.
    :license: MIT, see LICENSE for more details.
"""

import functools
from werkzeug.routing import Rule


def green_route(app, rule, **options):
    """
    :decorator function: green_route
        add url rule, map url rule 2 route functions

    :param app: the pirate app
    :param rule: the url rule
    """
    def decorator(f):
        if 'endpoint' not in options:
            options['endpoint'] = f.__name__
        app.url_map.add(Rule(rule, **options))  # add url rule
        app.route_functions[options['endpoint']] = f  # {'endpoint': func}
        return f
    return decorator
