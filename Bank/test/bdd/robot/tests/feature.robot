*** Settings ***

Documentation   Example Robot tests for Bank application to retrieve and update customer accounts

Resource        ../steps/resource.resource
Resource        ../steps/steps.resource

*** Test Cases ***

Retrieve customer balance
    Given I create the account 1111 with balance 50
    When I retrieve the account 1111
    Then the balance should be 50