import sys,os
if os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..')) not in sys.path:
    sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..')))
from selenium.webdriver.common.by import By
from common.PageElement import *
from robot.libraries.BuiltIn import BuiltIn

class PageLogin(PageElement):
    BUTTON_ACCEPT=(By.XPATH,"//*[text()='Accept']")

    def click_button_accept(self):
        self.click(locator=PageLogin.BUTTON_ACCEPT)



