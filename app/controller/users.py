from app.models.users import Users


class usersController:

    @staticmethod
    def addUser(user, passwd, email):
        Users(
            username=user,
            secret=passwd,
            email=email
        ).save()
