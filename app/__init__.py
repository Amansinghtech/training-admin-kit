from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/signin')
    def signin():
        return render_template('signin/signin.html')

    # Code goes here
    @app.route('/dashboard')
    def dashboard():
        return render_template("dashboard/dashboard.html")

    @app.route('/profile')
    def profile():
        return render_template('profile/profile.html')

    @app.route('/blank')
    def blank_page():
        return render_template('blank_page/pages-blank.html')

    @app.route('/signup')
    def signup():
        return render_template('signup/signup.html')

    return app
