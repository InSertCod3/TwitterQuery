import os
import sys
from flask import Blueprint, request, abort, jsonify, g

# Relative Imports
from . import BP_API
from .. import models


@BP_API.route('/users', methods=['POST', 'GET'])
def new_user():
    """ Base Class to Show all Users """
    return jsonify({'ERROR': "NOT IMPLEMENTED"})
