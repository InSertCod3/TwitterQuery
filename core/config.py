import os
import sys
import json

# Relative Imports
from . import utils

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

class Config(object):
    """[summary]

    Arguments:
        object {[type]} -- [description]
    """

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', None)

    try:
        TWITTER_CONSUMER_KEY = os.environ["TWITTER_CONSUMER_KEY"]
        TWITTER_CONSUMER_SECRET = os.environ["TWITTER_CONSUMER_SECRET"]
        TWITTER_ACCESS_TOKEN_KEY = os.environ["TWITTER_ACCESS_TOKEN_KEY"]
        TWITTER_ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
    except KeyError as APPLICATION_ENV_VAR_ERROR: 
        print("Please set the environment variable(s): ", APPLICATION_ENV_VAR_ERROR)
        sys.exit(1)


class DevelopmentConfig(Config):
    """Development Environment Configuration

    Arguments:
        Config {[type]} -- [description]
    """
    DEBUG = True


class ProductionConfig(Config):
    """Development Production Configuration

    Arguments:
        Config {[type]} -- [description]
    """
    DEBUG = False


class TestingConfig(Config):
    """Development Testing Configuration

    Arguments:
        Config {[type]} -- [description]
    """
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
