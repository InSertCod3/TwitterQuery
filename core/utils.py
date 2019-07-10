import os
from flask import url_for as real_url_for

def url_for(*args, **kwargs):
    """ Static Url helpper for html pages """
    return real_url_for(*args, **kwargs)
