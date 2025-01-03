from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="John",
                                     middlename="A.",
                                     lastname="Doe",
                                     nickname="JD",
                                     title="petr",
                                     company="Piter Company",
                                     address="frgsdgsdg",
                                     home="+700000000",
                                     mobile="+7111111111",
                                     work="+722222222",
                                     fax="+733333333",
                                     email="john.doe@example.com",
                                     bday="10",
                                     bmonth="July",
                                     byear="1980",
                                     aday="12",
                                     amonth="October",
                                     ayear="1985"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="",
                                     middlename="",
                                     lastname="",
                                     nickname="",
                                     title="",
                                     company="",
                                     address="",
                                     home="",
                                     mobile="",
                                     work="",
                                     fax="",
                                     email="",
                                     bday="",
                                     bmonth="-",
                                     byear="",
                                     aday="",
                                     amonth="-",
                                     ayear=""))
    app.session.logout()
