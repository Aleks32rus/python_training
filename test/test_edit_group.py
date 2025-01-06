# -*- coding: utf-8 -*-

from model.group import Group


def test_edit_group(app):
    app.group.edit_first_group(Group(name="123", header="456", footer="789"))


def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="321"))


def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="654"))