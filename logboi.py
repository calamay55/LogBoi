#!/usr/bin/env python
from selenium import webdriver
# We'll probably find other pieces of selenium useful, but for now that's fine
import properties


class MibbitBrowser:
    def __init__(self):
        pass

    def load_webdriver(self):
        pass

    def log_in_to_mibbit(self):
        pass

    def navigate_to_logs_page(self):
        pass

    def find_log_element(self):
        pass

    def copy_log_to_file(self):
        pass

    def turn_on_logboi(self):
        self.load_webdriver()
        self.log_in_to_mibbit()
        self.navigate_to_logs_page()
        # Run the next parts in a loop to copy every log, probably with some
        # arguments
        self.find_log_element()
        self.copy_log_to_file()


m = MibbitBrowser()
m.turn_on_logboi()
