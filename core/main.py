import os
import sys
from flask import Blueprint, render_template

# Relative Imports
from .utils import url_for

BP_MAIN = Blueprint('main', __name__)


@BP_MAIN.route('/')
def index():
    """Serve client-side application."""
    return render_template('index.html')

@BP_MAIN.route('/search', methods=['POST', 'GET'])
def search():
    """Serve client-side /search."""
    return render_template('search.html')

