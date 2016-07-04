# coding: utf-8
"""
    resp.py
    ```````

    pirate response class
"""

from werkzeug.wrappers import Response


class PirateResponse(Response):
    """
    :class PirateResponse:
        the response object used by default in pirate,
        but set default content-type as 'application/json'
    """
    content_type = 'application/json'
