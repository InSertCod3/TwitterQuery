import os
import sys
import fire

# Relative Imports
from core import app

class Tool(object):
    """Base Class to Run Cli commands"""

    def runserver(self):
        """Runs the App Using Config"""
        return app()


if __name__ == "__main__":
    fire.Fire(Tool)
