from flask import Blueprint, request, render_template
from app.controller.users import usersController
signup = Blueprint('singup', __name__)


@signup.route('/signup', methods=['GET', 'POST'])
def signup_index():
    if request.method == 'GET':
        return render_template('singup.html')

    if request.method == 'POST':
        data = dict(request.form)
        print(data)
        usersController.addUser(
            data['username'], data['passwd'], data['email'])
        return "hello world"
