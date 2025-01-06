from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test123", lastname="test456"))
    app.contact.edit_first_contact(Contact(firstname="John",
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

def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test123", lastname="test456"))
    app.contact.edit_first_contact(Contact(firstname="Elvin"))

def test_edit_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test123", lastname="test456"))
    app.contact.edit_first_contact(Contact(middlename="B."))