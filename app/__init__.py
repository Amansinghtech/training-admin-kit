from flask import Flask, render_template
from .routes.dashboard.view import dashboard
from .routes.profile.view import profile
from flask_mongoengine import MongoEngine
from .config import dev
from .routes.entrance.view import signup


def create_app():
    app = Flask(__name__)
    app.register_blueprint(dashboard)
    app.register_blueprint(profile)
    app.config.from_object(dev)
    db = MongoEngine(app)

    @app.route('/')
    @app.route('/signin')
    def signin():
        return render_template('signin/signin.html')

    app.register_blueprint(signup)
    return app
