#Session 20 - Selenium Pytest Integration
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager

import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class Browser:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    useremail_loc = (By.ID, 'email')
    password_loc = (By.ID, 'password')
    login_btn_loc = (By.ID, "login-btn")
    forgotpasswd_loc = (By.XPATH, "div[@class='forgot-password']/a[@class='forgot-password-link']")

    #     # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def __init__(self, url):
        self.url = url

    def launch_application(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            return True
        except Exception as e:
            print("Error in launching Website")
            return False

    def get_title(self):
        if self.launch_application():
            return self.driver.title
        else:
            print(self.url)
            raise Exception("Error! Page URL could not be found due to Browser issue")
            #return "Error! Page URL could not be found due to Browser issue"


    def get_url(self):
        if self.launch_application():
            return self.driver.current_url
        else:
            print(self.driver.current_url)
            raise Exception ("Error! Page URL could not be found due to Browser issue")

    def login_page(self):
        try:
            time.sleep(3)
            button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

            self.driver.find_element(By.ID, "email").send_keys("gayathribv@gmail.com")
            self.driver.find_element(By.ID, 'password').send_keys("B0rnanew*123")
            self.driver.find_element(By.ID, "login-btn").click()
            return self.driver.current_url
            print("Test Pass. Login button clicked")
        except NoSuchElementException:
            print("Test failed. Login button not found")


        # try:
        #     self.driver.find_element(*self.password_loc).send_keys("B0rnanew*123")
        # except NoSuchElementException:
        #     print("Unable to locate password input textbox")
        #
        # try:
        #     self.driver.find_element(*self.login_btn_loc).click()
        #     prod_element = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Our Products')]")
        #     return prod_element.is_displayed()
        #
        # except NoSuchElementException:
        #     print("Unable to locate login button")
        #


    def close_browser(self):
        self.driver.quit() # Close all instances of browsers
        # self.driver.close() # Close present instance opened by seleniul

if __name__ == '__main__':
    url='https://www.guvi.in/'
    my_browser = Browser(url)
    pgtitle=my_browser.get_title()
    if pgtitle == 'HCL GUVI | Learn to code in your native language':
        print("Test Passed, Page Title Verification Complete")
    else:
        print("Test Failed, Page Title Verification Failed")

    pgurl=my_browser.get_url()
    if pgurl == url:
        print("Test Passed. Page URL verification complete")
    else:
        print("Test Failed. Page URL could not be verified")
    time.sleep(2)
    my_browser.close_browser()