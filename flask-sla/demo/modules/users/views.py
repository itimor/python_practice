# -*- coding: utf-8 -*-
# author: itimor

# coding:utf-8

from flask import Blueprint, request, redirect, url_for
from flask import render_template
from flask_login import login_user, logout_user
from demo import login_manager
from demo.common.encrypt import md5
from models.users import User
from forms.users import LoginForm
from forms.register import RegisterForm
from demo.common import db
from flask import flash

userRoute = Blueprint('user',
                      __name__,
                      url_prefix='/user',
                      template_folder='templates',
                      static_folder='static')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@userRoute.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('login.html', form=form)
        user = User.query.filter(User.accountNumber == form.accountNumber.data,
                                 User.password == md5(form.password.data)).first()

        if user:
            login_user(user)
            return redirect("/")

    return render_template('login.html', form=form)


@userRoute.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.login'))


@userRoute.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('register.html', form=form)

        user = User.query.filter(User.accountNumber == form.accountNumber.data).first()

        if user:
            flash("The account is exist!")
            return render_template('register.html', form=form)

        user = User()
        user.accountNumber = form.accountNumber.data
        user.password = md5(form.password.data)
        user.name = form.name.data

        db.session.add(user)
        db.session.commit()

        return render_template('login.html', form=form)

    return render_template('register.html', form=form)
