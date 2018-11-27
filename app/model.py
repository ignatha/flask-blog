import datetime
import peewee as pw
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash

database = pw.SqliteDatabase('test.db')

class BaseModel(pw.Model):
    class Meta:
        database = database

class User(UserMixin,BaseModel):
    username = pw.CharField(unique=True)
    email = pw.CharField(unique=True)
    password = pw.CharField(max_length=100)
    joined_at = pw.DateTimeField(default=datetime.datetime.now)
    is_admin = pw.BooleanField(default=False)

    class Meta:
        order_by = ('-joined_at',)

    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            cls.create(
                username=username,
                email=email,
                password=generate_password_hash(password),
                is_admin=admin
            )
        except pw.IntegrityError:
            raise ValueError("User already exists")

