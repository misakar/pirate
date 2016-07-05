# coding: utf-8
"""
    pirate-orm
    ``````````

    adds basic SQLAlchemy support for pirate application
"""

from __future__ import absolute_import
import os
import re
import sys
import time
import functools
import warnings
import sqlalchemy
from math import ceil
# from flask import _request_ctx_stack, abort, has_request_context, request
from src.route import _request_ctx_hub, request
# from flask.signals import Namespace
from math import ceil  # 向上取整
from operator import itemgetter
from threading import Lock
from sqlalchemy import orm, event, inspect
from sqlalchemy.orm.exc import UnmappedClassError
from sqlalchemy.orm.session import Session as SessionBase
from sqlalchemy.engine.url import make_url
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from ._compat import iteritems, itervalues, xrange, string_types
