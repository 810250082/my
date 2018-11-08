# -*- coding:utf-8 -*-

from . import test
from model.user import User
from model.role import Role
from start import db


@test.route('/print-user')
def print_user():
    user = User()
    return str(user)


@test.route('/add-role')
def add_role():
    role = Role('运维')
    db.session.add(role)
    db.session.commit()
    return 'ok'


@test.route('/add-user')
def add_user():
    user_list = [
                    {'username': '石头', 'role_id':1},
                    {'username': '李磊', 'role_id':1},
                    {'username': '老鼠', 'role_id':2},
                    {'username': '冯巩', 'role_id':3},
                    {'username': '西施', 'role_id':2},
                    {'username': '悟空', 'role_id':3},
                ]
    for item in user_list:
        user = User(**item)
        db.session.add(user)

    db.session.commit()
    return 'ok'


@test.route('/select-user')
def select_user():
    user = User.query.filter_by(username='石头').first()
    return str(user)


@test.route('/select-role')
def select_role():
    role = Role.query.get(1)
    for user in role.users:
        id = user.id
    return str(role)

