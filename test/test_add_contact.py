from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="John",
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
                      ayear="1985")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="",
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
                      ayear="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
