import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate



def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
   
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # register the database commands
    from src import db

    db.init_app(app)
    migrate = Migrate(app, db)

    from src import technician
    from src import filex
    from src import station
    from src import tech_measurement
    from src import non_ionizing_radiation
    from src import users


    app.register_blueprint(technician.bp)
    app.register_blueprint(filex.bp)
    app.register_blueprint(station.bp)
    app.register_blueprint(tech_measurement.bp)
    app.register_blueprint(non_ionizing_radiation.bp)
    app.register_blueprint(users.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app
