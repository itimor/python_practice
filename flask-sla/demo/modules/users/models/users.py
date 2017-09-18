# coding:utf-8
from flask_login import UserMixin
from demo.common import db

class User(db.Model, UserMixin):
    """
    用户实体信息
    Attributes:
        id:用户编号。
        accountNumber:账号。
        password:密码。
        name:用户昵称。
    """
    id = db.Column(db.Integer, primary_key=True)
    accountNumber = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(20), unique=True)

    __tablename__ = 'sla_user'

    def __init__(self, user_id=None, account_number=None, password=None, name="anonymous"):
        """
        初始化用户信息。
        Args:
            user_id (int): 用户编号
            account_number(string):账号
            password(string):密码
            name (string):昵称
        """
        self.id = user_id
        self.accountNumber = account_number
        self.password = password
        self.name = name


class Permission:
    READ = 0x01
    CREATE = 0x02
    UPDATE = 0x04
    DELETE = 0x08
    DEFAULT = READ