from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from selenium.webdriver.support.select import Select

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome(executable_path=r'C:\Windows\SysWOW64\chromedriver.exe')
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()