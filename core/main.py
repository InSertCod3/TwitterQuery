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
