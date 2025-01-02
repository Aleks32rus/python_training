# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="trgwtgds", header="rgewgerg", footer="efwerfwre"))
    app.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
