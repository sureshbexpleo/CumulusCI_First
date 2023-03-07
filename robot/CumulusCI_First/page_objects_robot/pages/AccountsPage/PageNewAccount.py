import sys,time,os
if os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..')) not in sys.path:
    sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..')))
from selenium.webdriver.common.by import By
from common.PageElement import *
from robot.api.deco import keyword

class PageNewAccount(PageElement):

    BUTTON_NEW=(By.XPATH,"//a/div[@title='New']")
    BUTTON_NEXT=(By.XPATH,"//span[text()='Next']//parent::button")
    ERROR_MESSAGE=(By.XPATH,"//*[@class='pageLevelErrors' or @class='fieldLevelErrors']")
    ERROR_MESSAGE_LIST=(By.XPATH,"//ul[contains(@class,'errorsList')]")
    BUTTON_CANCEL=(By.XPATH,"//button[contains(@class, 'slds-button') and (@title='Cancel')]")
    BUTTON_SAVE_AND_NEW=(By.XPATH,"//button[contains(@class, 'slds-button') and (@title='Save and New')]")
    BUTTON_SAVE=(By.XPATH,"//button[@title='Save']")
    INPUT_INDIVIDUAL=(By.XPATH,"//input[@placeholder='Search Individual']")
    SUCCESS_MESSAGE=(By.XPATH,"//span[@class='toastMessage slds-text-heading--small forceActionsText']")




    @keyword(name='Select Record Type')
    def select_record_type(self,record_type):
        radio_button=self.explicit_wait(locator=(By.XPATH,f"//*[text()='{record_type}']"))
        radio_button.click()


    @keyword(name='Success Message Should be displayed')
    def success_message(self):
        try:
            self.explicit_wait(condition=EC.visibility_of_element_located,locator=PageNewAccount.SUCCESS_MESSAGE)
        except:
            raise Exception('Success Message is not visible')

    def get_input_field(self, item_name):
        return self.explicit_wait(locator=(By.XPATH,f"//label/span[text()='{item_name}']/../..//input"))

    def get_select_field(self, item_name):
        self.explicit_wait(locator=(By.XPATH,f"//span[text()='{item_name}']//parent::span//following-sibling::div//a"))
        self.scroll_to_element(locator=(By.XPATH,f"//span[text()='{item_name}']//parent::span//following-sibling::div//a"))
        return self.explicit_wait(locator=(By.XPATH,f"//span[text()='{item_name}']//parent::span//following-sibling::div//a"))

    def get_select_option(self, option):
        """dropdown of select field has to be open"""
        return self.explicit_wait(locator=(By.XPATH, f"//a[@title='{option}']"))

    def get_select_option_account(self, option):
        return self.explicit_wait(locator=(By.XPATH, f"//*[@role='menuitemradio'][@title='{option}']"))

    def input_value_of_item(self, item_name, value):
        input = self.get_input_field(item_name)
        input.click()
        input.clear()
        input.send_keys(value)

    def select_value_of_item(self, item_name, value):
        item = self.get_select_field(item_name)
        self.click_by_js(webelement=item)
        self.click_by_js(webelement=self.get_select_option(value))

    def select_value_of_item_given(self, item, value):
        self.click_by_js(webelement=item)
        self.click_by_js(webelement=self.get_select_option_account(value))

    @keyword(name='Fill Account Information')
    def fill_mandatory_account_information(self, salutation=None, first_name=None, last_name=None, we_user_id=None,
                                           email=None, mobile=None, sharing_criteria=None):
        if salutation is not None:
            self.select_value_of_item("Salutation", 'Mr.')
        if first_name is not None:
            self.input_value_of_item("First Name", first_name)
        if last_name is not None:
            self.input_value_of_item("Last Name", last_name)
        if we_user_id is not None:
            self.input_value_of_item("We User Id (Contact)", we_user_id)
        if email is not None:
            self.input_value_of_item("Email", email)
        if mobile is not None:
            self.input_value_of_item("Mobile", mobile)
        if sharing_criteria is not None:
            self.select_value_of_item("Sharing Criteria", sharing_criteria)

    @keyword(name='Click New Account')
    def click_new(self):
        self.click(locator=PageNewAccount.BUTTON_NEW)


    @keyword(name='Click Next In Select Record Type')
    def click_next(self):
        self.click_by_js(locator=PageNewAccount.BUTTON_NEXT)


    def click_cancel(self):
        self.click(locator=PageNewAccount.BUTTON_CANCEL)


    def click_save_and_new(self):
        self.click(locator=PageNewAccount.BUTTON_SAVE_AND_NEW)


    @keyword(name='Click Save Button')
    def click_save(self):
        self.click(locator=PageNewAccount.BUTTON_SAVE)


    def snag_error_message(self, message=None):
        return self.explicit_wait(locator=(By.XPATH,f'//div[text()="{message}"]'))


    def review_error_fields_list(self):
        return self.explicit_wait(locator=(By.XPATH,"//ul[contains(@class,'errorsList')]//li")).text


    def get_errormessage_required_fields(self):
        return self.explicit_wait(locator=(By.XPATH,"//div//ul[@class='errorsList']/li[contains(text(),'required fields')]")).text