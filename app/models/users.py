import mongoengine as me
from flask_bcrypt import generate_password_hash, check_password_hash


class Users(me.Document):
    username = me.StringField(required=True)
    fname = me.StringField(required=True)
    lname = me.StringField(required=True)
    phone = me.IntField(required=True)
    email = me.EmailField(required=True)
    secret = me.StringField(required=True)
    info = me.DictField()

    def genPassHash(self):
        self.secret = generate_password_hash(self.secret).decode('utf-8')
        return self.secret

    def checkPassHash(self, secret):
        return check_password_hash(pw_hash=self.secret, password=secret)

    def save(self, *args, **kwargs):
        self.genPassHash()
        return super(Users, self).save(*args, **kwargs)
