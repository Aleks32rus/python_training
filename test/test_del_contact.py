from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test123", lastname="test456"))
    app.contact.del_first_contact()
