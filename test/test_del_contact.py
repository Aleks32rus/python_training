from model.contact import Contact


def test_del_contact(app):
    app.contact.del_first_contact()
