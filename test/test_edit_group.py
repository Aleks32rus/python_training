# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="123", header="456", footer="789"))
    app.session.logout()
