#!/usr/bin/env python
import time
from getpass import getpass
from selenium import webdriver
# We'll probably find other pieces of selenium useful, but for now that's fine
import xpaths


class MibbitBrowser:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def load_website(self):
        self.driver.get("https://client00.chat.mibbit.com/")
        # It may be useful to add code to try out client01 and client02
        # if this fails

    def log_in_to_mibbit(self):
        login_link = self.driver.find_element_by_xpath(xpaths.login_link)
        login_link.click()
        time.sleep(1)  # Give the modal a second to come into view
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(
            xpaths.login_frame))
        username_input_box = self.driver.find_element_by_xpath(xpaths.username)
        username_input_box.send_keys(input("Username: "))
        password_input_box = self.driver.find_element_by_xpath(xpaths.password)
        password_input_box.send_keys(getpass("Password: "))
        login_button = self.driver.find_element_by_xpath(xpaths.login_button)
        login_button.click()
        time.sleep(3)  # Mibbit needs time for the login to actually occur
        self.driver.switch_to.default_content()

    def navigate_to_logs_page(self):
        logs_panel_link = self.driver.find_element_by_xpath(
            xpaths.logs_panel_link)
        logs_panel_link.click()
        logs_tab = self.driver.find_element_by_xpath(xpaths.logs_tab)
        logs_tab.click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(
            xpaths.logs_frame))
        channel_logs_link = self.driver.find_element_by_xpath(
            xpaths.channel_logs_link)
        channel_logs_link.click()

    def copy_logs_to_files(self):
        pass

    def turn_on_logboi(self):
        self.load_website()
        self.log_in_to_mibbit()
        self.navigate_to_logs_page()
        self.copy_logs_to_files()


m = MibbitBrowser()
m.turn_on_logboi()
