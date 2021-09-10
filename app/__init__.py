from re import A
from flask import Flask, render_template
from .routes.dashboard.view import dashboard
from .routes.profile.view import profile


def create_app():
    app = Flask(__name__)
    app.register_blueprint(dashboard)
    app.register_blueprint(profile)

    @app.route('/')
    @app.route('/signin')
    def signin():
        return render_template('signin/signin.html')

    @app.route('/blank')
    def blank_page():
        return render_template('blank_page/pages-blank.html')

    @app.route('/signup')
    def signup():
        return render_template('signup/signup.html')

    @app.route('/charts')
    def charts():
        return render_template('charts/chart.html')
    return app
