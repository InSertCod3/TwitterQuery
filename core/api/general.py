import os
import sys
from flask import Blueprint, request, abort, jsonify, g
import twitter

# Relative Imports
from . import BP_API
from ..config import Config

api = twitter.Api(consumer_key=Config.TWITTER_CONSUMER_KEY,
                  consumer_secret=Config.TWITTER_CONSUMER_SECRET,
                  access_token_key=Config.TWITTER_ACCESS_TOKEN_KEY,
                  access_token_secret=Config.TWITTER_ACCESS_TOKEN_SECRET)

def key_missing_checker(data, keys):
    _schema = {"status": "ok", "message": "ok", "data": None}
    for k in keys:
        if k not in data.keys():
            _schema = {**_schema, **{"status": "error", "message": "required field '{0}' is missing.".format(k)}}
            continue
        if data[k] is None or data[k] == "":
            _schema = {**_schema, **{"status": "error", "message": "required field '{0}' cannot be 'None'.".format(k)}}
    return _schema

@BP_API.route('/tweet/search', methods=['GET'])
def twitter_search():
    """
    Base for user and twitter search.
    
    Returns:
        jsonify -- jsonify(...)
    """
    _schema = {"q": None, "count": 50, "max_id": None, "include_entities": None}
    _bind = {**_schema, **request.args}
    _kc = key_missing_checker(_bind, ["q"])
    if _kc["status"] == "error":
        return jsonify(_kc)
    _kc["data"] = api.GetSearch(term=_bind['q'],
                                count=_bind['count'],
                                result_type="recent",
                                max_id=_bind['max_id'],
                                include_entities=_bind['include_entities'],
                                return_json=True)
    return jsonify(_kc)
