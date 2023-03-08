import sys,os
if os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..')) not in sys.path:
    sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..')))

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from robot.libraries.BuiltIn import BuiltIn
from common.PageElement import PageElement


class PageNewReport(PageElement):
    BUTTON_CLEAR=(By.XPATH,"//button/*[text()='Clear']")
    BUTTON_NEW_REPORT=(By.XPATH,"//div[@title='New Report']")
    SEARCH_REPORT_TYPE=(By.XPATH,"//input[@id='modal-search-input']")
    BUTTON_ACCEPT=(By.XPATH,"//*[text()='Accept']")

    def click_button_new_report(self):
        self.explicit_wait(wait=60, condition=EC.visibility_of_element_located,locator=PageNewReport.BUTTON_NEW_REPORT)
        self.click_by_js(locator=PageNewReport.BUTTON_NEW_REPORT)

    def click_accept(self):
        self.click(locator=PageNewReport.BUTTON_ACCEPT)

    def result_report_type(self,report_name):
        return self.get_web_element_by_xpath(f"//a/*[@data-tooltip='{report_name}']")

    def check_report_type_name(self,report_name,filter='All'):
        self.explicit_wait(wait=120, condition=EC.frame_to_be_available_and_switch_to_it, locator=(By.XPATH,"//iframe[@title='Report Builder']"))
        print("Switched to Iframe")
        filter_element=self.explicit_wait(wait=120, condition=EC.presence_of_element_located,locator=(By.XPATH, f"//li/*[text()='{filter}']"))
        filter_element.click()
        self.click(locator=PageNewReport.BUTTON_CLEAR)

        self.send_keys_char_by_char(locator=PageNewReport.SEARCH_REPORT_TYPE,value=report_name)
        try:
            if not self.check_visible(locator=(By.XPATH,f"//a/*[@data-tooltip='{report_name}']")):
                raise Exception(report_name+' is not visible')
        finally:
            self.switch_to_default_content()