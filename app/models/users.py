import mongoengine as me


class Users(me.Document):
    username = me.StringField(required=True)
    fname = me.StringField(required=True)
    lname = me.StringField(required=True)
    phone = me.IntField(required=True)
    email = me.EmailField(required=True)
    secret = me.StringField(required=True)
    info = me.DictField()
