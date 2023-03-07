*** Settings ***
Library  SeleniumLibrary
Library    ../page_objects_robot/pages/LoginPage/PageLogin.py
Library    ../page_objects_robot/web_driver/WebDriverManager.py
Library    PageLogin.PageLogin    ${browser}     ${url}     ${user}     WITH NAME    obj

*** Keywords ***
Click Accept
    click button accept

Open my browser
    [Arguments]    ${browser}   ${url}  ${user}
    P   ${browser}   ${url}  {user}
    maximize browser window
    quit

