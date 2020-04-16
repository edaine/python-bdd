from behave import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp

from app.bank_app import app, BANK
from app.account import Account


@given(u'I create account "{account_number}" with balance of "{balance}"')
def i_create_account_with_balance_of_group1(context, account_number, balance):
    a = Account(account_number, balance)
    BANK.add_account(a)


@given(u'I visit the homepage')
def i_visit_the_homepage(context):
    context.browser = TestApp(app)
    context.browser.response = context.browser.get('http://localhost:5000/')
    assert_equal(context.browser.response.status_code, 200)
    # assert_equal(context.browser.response.text, 'Hello World!')


@when(u'I enter the account number "{account_number}"')
def when_i_enter_the_account_number_group1(context, account_number):
    form = context.browser.response.forms['account-form']
    form['account_number'] = account_number
    context.browser.form_response = form.submit()
    assert_equal(context.browser.form_response.status_code, 200)


@then(u'I see a balance of "{expected_balance}"')
def then_i_see_a_balance_of_group1(context, expected_balance):
    assert_in("Balance: {}".format(expected_balance),
              context.browser.form_response.text)
