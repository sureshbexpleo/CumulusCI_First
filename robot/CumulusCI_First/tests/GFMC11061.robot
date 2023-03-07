*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Library    Screenshot
Library    ./launcher.py
Library    ../page_objects_robot/pages/LoginPage/PageLogin.py
Library    ../page_objects_robot/pages/HomePage/PageHome.py
Library    ../page_objects_robot/pages/ReportPage/PageNewReport.py

*** Variables ***
${cert_name}     Systemuser_ONECRM-Testa_CEMBusinessadmin
${url}  https://login-qs.vwgroup.com/isam/sps/idpextqs/saml20/logininitial?RequestBinding=HTTPPost&PartnerId=https://vwg5-vwgroup--qa.sandbox.my.salesforce.com
${REPORT_MODULE}    Reports
@{REPORT_NAMES}     Accounts with Opportunities     Contacts with Opportunities     Account with Asset with Opportunity     Contact Point Type Consent      Individual with Contact     Individual with Lead        Data Use Purpose
*** Test Cases ***
TestCase_GFMC10649
    ${options} =    Create Profile   ${cert_name}
    ${profile_path} =    Get Certificate Path   ${cert_name}
    open browser    ${url}        firefox  ff_profile_dir=${profile_path}  options=${options}
    Wait Till Home Page Load Completes
    capture page screenshot
    Open Module From App Launcher    ${REPORT_MODULE}
    capture page screenshot
    click button new report
    capture page screenshot

    FOR     ${report_name}  IN  @{REPORT_NAMES}

        check report type name      ${report_name}
        log to console    ${report_name}
        capture page screenshot
    END
    Close browser