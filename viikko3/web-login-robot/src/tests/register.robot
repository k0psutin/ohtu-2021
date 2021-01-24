*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Enter Full Information  abcde  kalle123
    Submit Registration
    Page Should Contain  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Enter Full Information  a  kalle123
    Submit Registration
    Page Should Contain  Username length should be 3 at minimum

Register With Valid Username And Too Short Password
    Enter Full Information  abcde  kalle
    Submit Registration
    Page Should Contain  Password length should be 8 at minimum

Register With Nonmatching Password And Password Confirmation
    Input Text  username  abcde
    Input Text  password  kalle123
    Input Text  password_confirmation  kalle132
    Submit Registration
    Page Should Contain  Passwords doesn't match

Login After Successful Registration
    Enter Full Information  abcde  asdasdasd1
    Submit Registration
    Go To Login Page
    Set Username  abcde
    Set Password  asdasdasd1
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Enter Full Information  abcde  asd
    Submit Registration
    Go To Login Page
    Set Username  abcde
    Set Password  asd
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

