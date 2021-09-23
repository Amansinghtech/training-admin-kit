from app.models.users import Users


class usersController:

    @staticmethod
    def addUser(data):
        result = Users(
            username=data['username'],
            secret=data['passwd'],
            email=data['email'],
            fname=data['fname'],
            lname=data['lname'],
            phone=data['phone']
        ).save()
        return result

    @staticmethod
    def getUser(username):

        result = Users.objects.get(username=username)
        if result:
            return result
        else:
            return False

    @staticmethod
    def getAllUsers():
        result = Users.objects()
        if result:
            return result
        else:
            return False

    @staticmethod
    def deleteUser():
        result = Users.objects(id="614b2e45c3cc729e65b6f928").delete()
        return result
