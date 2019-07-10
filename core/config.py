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
