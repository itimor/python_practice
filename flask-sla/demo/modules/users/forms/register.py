#coding:utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp


class RegisterForm(FlaskForm):
    accountNumber = StringField('accountNumber',  validators=[DataRequired('账号不可以是空的'),
                                                             Length(-1, 20, '账号的字符数不可以超过 20 个'),
                                                             Email('账号只能是邮箱')])
    password = PasswordField('password', validators=[DataRequired('密码不可以是空的'),
                                                     Length(6, 20, '密码的字符数只能在 6 - 20 个之间'),
                                                     Regexp(regex='[A-Za-z]+[\d+\W+]+',
                                                            message='为了密码复杂性,请输入大小写字母,数字,特殊符号,且开头必须为字母')])
    name = StringField('name', validators=[DataRequired('昵称不可以是空的'),
                                                     Length(3, 20, '昵称的字符数只能在 3 - 20 个之间')])