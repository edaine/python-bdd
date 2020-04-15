from behave import *
from nose.tools import assert_equal
from webtest import TestApp

from app.bank_app import app

@given('I visit the homepage')
def i_visit_the_homepage(context):
    browser = TestApp(app)
    browser.response = browser.get('http://localhost:5000/')
    assert_equal(browser.response.status_code, 200)
    assert_equal(browser.response.text, 'Hello World!')