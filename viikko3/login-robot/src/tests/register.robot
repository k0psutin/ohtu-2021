*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New User  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New User  kalle  kalle123
    Input New User  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New User  ka  kalle123
    Output Should Contain  Username length should be 3 at minimum

Register With Valid Username And Too Short Password
    Input New User  kaaa  kall14
    Output Should Contain  Password length should be 8 at minimum

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New User  kalle  aksjdhfg
    Output Should Contain  Password should contain numbers and letters