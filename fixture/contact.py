from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.add_new_contact()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//input[@value='Enter']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("mobile", contact.mobile)
        self.change_selected_value("bday", contact.bday)
        self.change_selected_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_selected_value("aday", contact.aday)
        self.change_selected_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

    def change_selected_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_first_contact(self):
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def add_new_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_xpath("//input[@value='Enter']")) > 0):
            wd.find_element_by_link_text("add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchform")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//img[@title='Edit']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("[name='entry']"):
                firstname = element.find_elements_by_css_selector("td")[2].text
                lastname = element.find_elements_by_css_selector("td")[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return self.contact_cache
