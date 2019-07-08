#!/usr/bin/env python
import os
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

    ''''
    The new destination is
    https://my.chat.mibbit.com/channellogs

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
    '''

    def navigate_to_logs_page(self):
        pass

    def copy_logs_to_files(self):
        self.driver.get("https://my.chat.mibbit.com/channellogs")
        time.sleep(1) # Let the alert pop up
        self.driver.switch_to.alert.accept()
        conv_list = self.driver.find_elements_by_css_selector('body > table.itable > tbody > tr:nth-child(2) > td:nth-child(2) > div > a')

        conv_numbers = []
        for element in conv_list:
            href = element.get_attribute("href")
            conv_number = href.split("=")[-1]
            if conv_number not in conv_numbers:
                conv_numbers.append(conv_number)

        conv_dates = {}
        for conv in conv_numbers:
            self.driver.get(f"https://my.chat.mibbit.com/channellogs?view=scd&server=3091&conv={conv}")
            dates = []
            dates_list = self.driver.find_elements_by_css_selector("body > table.itable > tbody > tr:nth-child(2) > td:nth-child(3) > div > a")
            for element in dates_list:
                href = element.get_attribute("href")
                date = href.split("=")[-1]
                if date not in dates:
                    dates.append(date)
            conv_dates[conv] = dates

        for conv in conv_dates.keys():
            self.driver.get(f"https://my.chat.mibbit.com/channellogs?view=scd&server=3091&conv={conv}")
            selected_conv = self.driver.find_element_by_xpath(xpaths.selected_conv)
            conv_name = selected_conv.text[1:]
            if not os.path.isdir(conv_name):
                os.mkdir(conv_name)
            dates = conv_dates[conv]
            for date in dates:
                self.driver.get(f"https://my.chat.mibbit.com/channellogs?view=scd&server=3091&conv={conv}&date={date}")
                logdiv = self.driver.find_element_by_xpath(xpaths.logdiv)
                text = logdiv.text
                stripped_chars = (c for c in text if 0 < ord(c) < 127)
                stripped_text = ''.join(stripped_chars)
                with open(f"{conv_name}//{date}.txt", "w+") as logfile:
                    logfile.write(stripped_text)


    def turn_on_logboi(self):
        self.load_website()
        self.log_in_to_mibbit()
        self.navigate_to_logs_page()
        self.copy_logs_to_files()


m = MibbitBrowser()
m.turn_on_logboi()
