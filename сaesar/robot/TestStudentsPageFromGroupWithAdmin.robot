*** Settings ***
Documentation     Check opportunity of opening student's list editor afterselecting group and click on button 'students'.
Suite Teardown    Close Browser
Library           Selenium2Library
Library           Collections
Resource          Resource/students_page_resource.robot

*** Test Cases ***
test19_opening_students_list_editor_after_selecting_group
    [Documentation]    Check opportunity of opening student's list editor afterselecting group and click on button 'students'.
    Open site
    LogIn by Administrator
    Select Group
    Click Students Button
    Click Edit Students List Button
    Element Should Be Enabled    xpath=//*[@id="modal-window"]/section//button[1]
