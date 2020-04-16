*** Settings ***
Documentation   Step definitions

*** Keywords ***
I create the account ${account_number} with balance ${balance}
    Create Account      ${account_number}   ${balance}

I retrieve the account ${account_number}
    Visit Homepage
    Retrieve Account    ${account_number}

The balance should be ${balance}
    Display Balance     ${balance}