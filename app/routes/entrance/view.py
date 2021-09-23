from flask import Blueprint, json, request, render_template, jsonify
from app.controller.users import usersController as UC
signup = Blueprint('singup', __name__)


@signup.route('/signup', methods=['GET', 'POST'])
def signup_index():
    if request.method == 'GET':
        return render_template('singup/singup.html')

    if request.method == 'POST':
        data = dict(request.form)
        print(data)
        UC.addUser(
            data['username'], data['passwd'], data['email'])
        return "hello world"


@signup.route('/test')
def test():
    user = {
        "username": "aman123",
        "fname": "aman",
        "lname": "singh",
        "phone": 1234567890,
        "email": "aman@newklio.com",
        "passwd": "aman@abc123"
    }

    test = UC.addUser(user)

    return 'test is running'


@signup.route('/getUser')
def getUser():
    test = UC.getUser('rica123')
    return jsonify(test)


@signup.route('/users')
def getAllUsers():
    test = UC.getAllUsers()
    return jsonify(test)


@signup.route('/deleteUser')
def deleteUser():
    test = UC.deleteUser()
    return jsonify(test)
