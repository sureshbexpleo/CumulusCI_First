import sys,os
if os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..')) not in sys.path:
    sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..')))
from selenium.webdriver.common.by import By
from common.PageElement import *
from robot.libraries.BuiltIn import BuiltIn


class PageHome(PageElement):

    BUTTON_ONE_APP_LAUNCHER=(By.XPATH,"//one-app-launcher-header//button")
    BUTTON_VIEW_ALL=(By.XPATH,"//button[text()='View All']")

    def click_one_app_launcher(self):
        self.click(locator=PageHome.BUTTON_ONE_APP_LAUNCHER)

    def click_view_all(self):
        self.click(locator=PageHome.BUTTON_VIEW_ALL)

    def open_module(self,module_name):
        self.explicit_wait(wait=60, condition=EC.element_to_be_clickable,locator=(By.XPATH, f"//*[@one-applaunchermodal_applaunchermodal]//a[@data-label='{module_name}']"))
        self.click_by_js(locator=(By.XPATH,f"//*[@one-applaunchermodal_applaunchermodal]//a[@data-label='{module_name}']"))
        # self.click(wait=20,locator=(By.XPATH,f"//*[@one-applaunchermodal_applaunchermodal]//a[@data-label='{module_name}']"))

    @keyword(name='Open Module From App Launcher')
    def open_module_in_app_launcher(self,module_name):
        self.click_one_app_launcher()
        self.click_view_all()
        self.open_module(module_name=module_name)

    @keyword(name='Wait Till Home Page Load Completes')
    def wait_till_home_page_load_completes(self):
        self.explicit_wait(wait=60,condition=EC.visibility_of_element_located,locator=(By.XPATH,"//*[@id='brandBand_2']"))