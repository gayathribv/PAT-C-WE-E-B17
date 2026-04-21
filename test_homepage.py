#Session 20 stopped at 2:26

from unittest import TestCase

from Seleniumwithvirtualenv import Browser
import time

url='https://www.guvi.in/'
browser = Browser('url')
my_browser = Browser(url)
url_neg = 'https://www.guvi.in'
my_neg_browser = Browser(url_neg)

class TestBrowser(TestCase):

    def testcase_title_validation(self):
        title_of_page = my_browser.get_title()
        if title_of_page == 'HCL GUVI | Learn to code in your native language':
            print("Test Passed. Page Title Verification complete")
        else:
            print("Test Failed. Page Title Verification Could not be Verified")
        time.sleep(5)
        # my_browser.close_browser()

    def testcase_url_validation(self):
        url_of_page = my_browser.get_url()
        if url_of_page == url:
            print("Test Passed. Page URL Verification complete")
        else:
            print("Test Failed. Page URL Verification Could not be Verified")
        time.sleep(3)
        #my_browser.close_browser()

    def testcase_login_positive(self):
        time.sleep(3)
        exp_url='https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F'
        act_url=my_browser.login_page()
        if exp_url == act_url:
            print("Login page access Complete. Testcase Passed")
        else:
            print("Unable to access login page. Testcase failed")



    def testcase_title_validation_negative(self):
        title_of_page = my_neg_browser.get_title()
        if title_of_page == 'HCL GUVI | Learn to code in your native language':
            print("Test Passed. Page Title Verification complete")
        else:
            print("Test Failed. Page Title Verification Could not be Verified")
        time.sleep(5)
        # my_browser.close_browser()

    def testcase_url_validation_negative(self):
        url_of_page = my_neg_browser.get_url()
        if url_of_page == url:
            print("Test Passed. Page URL Verification complete")
        else:
            print("Test Failed. Page URL Verification Could not be Verified")

    def testcase_login_positive(self):
        time.sleep(3)
        exp_url = 'https://www.guvi.in/'
        act_url = my_browser.login_page()
        if exp_url != act_url:
           print("Negative testing complete. Testcase Passed")
        else:
           print("Negative testing Testcase failed")

    time.sleep(5)
    my_browser.close_browser()