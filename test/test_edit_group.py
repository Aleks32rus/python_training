# -*- coding: utf-8 -*-

from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(name="123", header="456", footer="789"))


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(name="321"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(header="654"))