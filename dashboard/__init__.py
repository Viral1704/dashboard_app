from flask import Flask

from .routes.auth import auth
from .routes.main import main

from .commands import create_tables, create_products, create_orders, test_query

from .extensions import db

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    app.cli.add_command(create_tables)
    app.cli.add_command(create_products)
    app.cli.add_command(create_orders)
    app.cli.add_command(test_query)

    return app