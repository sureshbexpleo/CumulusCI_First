import os
import sys,time
if os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..')) not in sys.path:
    sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..')))

from common.PageElement import *
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC



class PageAccountDetailsView(PageElement):
    BUTTON_EDIT=(By.XPATH,"//div[contains(text(),'Account')]//ancestor::flexipage-component2//button[@name='Edit']")
    BUTTON_SAVE=(By.XPATH,"//div[contains(@class,'forceRecordEditActions')]//span[text()='Save']")
    BUTTON_SAVE_POPUP=(By.XPATH,"//*[contains(@class,'forceRecordEditActions')]//button/*[text()='Save']")

    @keyword(name='Click Edit Button')
    def click_edit(self):
        self.explicit_wait(locator=PageAccountDetailsView.BUTTON_EDIT).click()

    @keyword(name='Get All Options From Preferred Language Dropdown')
    def get_all_options_preferred_language(self):
        element=self.explicit_wait(locator=(By.XPATH,"//*[text()='Preferred Language']//parent::span//following-sibling::div//a"))
        element.click()
        options=self.driver.find_elements(By.XPATH,"(//div[contains(@class,'select-options popupTargetContainer')])[6]//li//a")
        list=[]
        for index in range(1,len(options)+1):
            title=self.explicit_wait(locator=(By.XPATH,"(//div[contains(@class,'select-options popupTargetContainer')])[6]//li["+str(index)+"]//a")).get_attribute('title')
            list.append(title)
        return list

    @keyword(name='Check Preferred Languages Are Present In Expected Dropdown')
    def check_dropdown(self,expected,actual):
        for exp_dropdown in expected:
            if not exp_dropdown in actual:
                raise Exception(f'{exp_dropdown} is not present in actual dropdown')