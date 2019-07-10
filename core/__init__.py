import os
import sys
from flask import Flask

# Relative Imports
from .config import config


def app(config_name="development"):
    """[summary]
    
    Keyword Arguments:
        config_name {[type]} -- [description] (default: {APP_CONFIG["app"]["config_name"]})
    
    Returns:
        [type] -- [description]
    """

    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')
    flask_app = Flask(__name__)
    flask_app.config.from_object(config[config_name])

    # Register web application routes
    from .main import BP_MAIN as main_blueprint
    flask_app.register_blueprint(main_blueprint)

    # Register API routes
    from .api import BP_API as api_blueprint
    flask_app.register_blueprint(api_blueprint, url_prefix='/api')

    return flask_app.run(host="0.0.0.0", port=5000, threaded=True)
