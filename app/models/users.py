import mongoengine as me


class Users(me.Document):
    username = me.StringField(required=True)
    email = me.EmailField(required=True)
    secret = me.StringField(required=True)
