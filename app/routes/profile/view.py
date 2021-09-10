from os import name
from flask import Blueprint, render_template

profile = Blueprint('user', __name__)


@profile.route('/profile')
def index():
    return render_template('profile/profile.html')


@profile.route('/profile/<string:name>')
def special_route(name):
    return render_template('profile/profile.html', user=name)
