*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Library    OperatingSystem
Library    Screenshot
Library    ./launcher.py
Library    ../page_objects_robot/pages/LoginPage/PageLogin.py
Library    ../page_objects_robot/pages/HomePage/PageHome.py
Library    ../page_objects_robot/pages/AccountsPage/PageNewAccount.py
Library    ../page_objects_robot/pages/AccountsPage/PageAccountDetailsView.py

*** Variables ***
${cert_name}     Systemuser_ONECRM-Testa_CEMBusinessadmin
${url}  https://login-qs.vwgroup.com/isam/sps/idpextqs/saml20/logininitial?RequestBinding=HTTPPost&PartnerId=https://vwg5-vwgroup--qa.sandbox.my.salesforce.com
${ACCOUNT_MODULE}    Accounts
${RECORD_TYPE}      Person Account
${SALUTATION}       Mr.
${FIRST_NAME}       QASDFCK
${LAST_NAME}        LJDHUIK
${WE_USER_ID}       jhfjfkk
${EMAIL}            temp@temp.com
@{EXPECTED_LANGUAGES}     Bosnian    Serbian  Bosnian (Bosnia and Herzegovina)  English (Cyprus)  English (Gibraltar)  Spanish (Canary Islands)  French (Réunion)  Russian (Estonia)  Russian (Lithuania)  Russian (Latvia)  Albannian (Macedonia)
*** Test Cases ***
TestCase_GFMC10649
    ${options} =    Create Profile   ${cert_name}
    ${profile_path} =    Get Certificate Path   ${cert_name}
    open browser    ${url}        firefox  ff_profile_dir=${profile_path}  options=${options}
    Wait Till Home Page Load Completes
    capture page screenshot
    Open Module From App Launcher     ${ACCOUNT_MODULE}
    Click New Account
    capture page screenshot
    Select Record Type      ${RECORD_TYPE}
    capture page screenshot
    Click Next In Select Record Type
    capture page screenshot
    ${RANDOM_WE_USER_ID} =	Get Random String Lower Case Value	${8}
    Fill Account Information    ${SALUTATION}   ${FIRST_NAME}   ${LAST_NAME}    ${RANDOM_WE_USER_ID}   ${EMAIL}    ${NONE}     ${NONE}
    capture page screenshot
    Click Save Button
    capture page screenshot
    Success Message Should be displayed
    capture page screenshot
    Click Edit Button
    @{ACTUAL_DROPDOWNS} =   Get All Options From Preferred Language Dropdown
    capture page screenshot
    Check Preferred Languages Are Present In Expected Dropdown      ${EXPECTED_LANGUAGES}       ${ACTUAL_DROPDOWNS}
    Close browser