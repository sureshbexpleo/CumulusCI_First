import sys
# if "C:\\Users\\10872\\.local\\pipx\\venvs\\cumulusci\\Lib\\site-packages" not in sys.path:
#     sys.path.append('C:\\Users\\10872\\.local\\pipx\\venvs\\cumulusci\\Lib\\site-packages')
from cumulusci.robotframework.pageobjects import ListingPage, pageobject


@pageobject(page_type='Listing', object_name='AccountObject__c')
class CustomObjectListingPage(ListingPage):
    pass