#!/usr/bin/python3
# -*- coding: utf-8 -*-

# The simplest decorator to json

# D.Plotnikov 2021

import json
from functools import wraps

def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = json.dumps(func(*args, **kwargs))
        return res
    return wrapper

