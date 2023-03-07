*** Settings ***
Library    SeleniumLibrary
Resource    ../resource/LoginKeywords.robot

*** Variables ***
${browser}  firefox
${url}  https://login-qs.vwgroup.com/isam/sps/idpextqs/saml20/logininitial?RequestBinding=HTTPPost&amp;PartnerId=https://vwg5-vwgroup--qa.sandbox.my.salesforce.com
${user}     Systemuser_ONECRM-Testa_CEMBusinessadmin


*** Test Cases ***
LoginTest
    Open my browser    ${browser}   ${url}  ${user}
    close all browsers