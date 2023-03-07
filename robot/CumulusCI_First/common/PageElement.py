from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class PageElement(object):


    def __init__(self):
        try:
            self.driver = BuiltIn().get_library_instance('SeleniumLibrary').driver
        except:
            self.driver=None

        self.time_out=120
        self._wait = WebDriverWait(self.driver, self.time_out)

    def get_web_element_by_xpath(self, xpath):
        return self._wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def get_web_elements_by_xpath(self, xpath):
        return self._wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def explicit_wait(self,wait=10,condition=EC.presence_of_element_located,locator=None):
        if wait is not None:
            self.time_out=wait
        return self._wait.until(condition((locator)))

    def send_keys_char_by_char(self, locator=None,value=None):
        for char in list(value):
            input=self.explicit_wait(locator=locator)
            input.send_keys(char)

    def send_keys(self, locator=None,value=None):
        input=self.explicit_wait(locator=locator)
        input.send_keys(value)

    def click(self,wait=10,locator=None):
        ele = self.explicit_wait(wait=wait,locator=locator)
        try:
            ele.click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            self.click_by_js(locator=locator)
            print('Click not working')

    def click_by_js(self,locator=None,webelement=None):
        if locator is None:
            ele=webelement
        else:
            ele = self.explicit_wait(locator=locator)
        self.driver.execute_script("arguments[0].click();", ele)

    def scroll_to_element(self,locator):
        ele = self.explicit_wait(locator=locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def clear(self,locator):
        button = self.explicit_wait(locator=locator)
        button.clear()

    def check_visible(self, locator=None):

        try:
            self.explicit_wait(wait=10,condition=EC.visibility_of_element_located,locator=locator)

        except (ElementNotVisibleException, NoSuchElementException):
            return False
        else:
            return True

    def switch_to_frame(self,locator=None):
        self._wait.until(EC.frame_to_be_available_and_switch_to_it(locator))

    def switch_to_default_content(self):
        """        Switch to Main Content   """
        self.driver.switch_to.default_content()

    def get(self, url):
        self.driver.get(url)

    def close_all(self):
        self.driver.quit()

