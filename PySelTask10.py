# Visit te URL https://saucedemo.com. and login with the following credentials
#         Username: standard_user
#         password: secret_sauce
#
# Try to fetch the following using Python Selenium:-
#     1. Title of the Webpage
#     2. Current URL of the Webpage
#     3. Extra the entire contents of the webpage and save it in a Text File
#        whose name will be "Webpage_task.txt"
#
# After completing the Selenium generate Pytest based test_case reports for both
# Positive and Negative Test-cases based on the :-
#     1. Title of web application
#     2. URL of the Homepage
#     3. URL of the Dashboard after Login with credentials given above
#
# Note:
#     1. Create a Python file with a .py extension and save the code in that file
#     2. Pytest test-case files in the HTML Format is mandatory

# Import necessary packages

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

#setup the webdriver

options = Options()
# Not using for now as not aware of this might work
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver.webdriver.Chrome(Options=options)

#Open demo webbrowser
driver.get("https://www.saucedemo.com")
#sleep to let all the webelements load
sleep(3)

page_title = driver.title
assert "Swag Labs" in page_title
print("TEST 0: 'title' test passed")

#Extract Page content and save to file
page_source = driver.page_source
with open("Webpage_task.txt", "w", encoding="utf-8") as file:
    file.write(page_source)
#Log in using login and passwd
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
text = driver.find_element(By.CLASS_NAME, "title").text
assert "products" in text.lower()
print("TEST PASSED : LOGIN SUCCESSFUL")

dashboard_title = driver.find_element(By.CLASS_NAME, "title").text
print("Dashboard title is",dashboard_title)
#Close the session and quit the webbrowser
driver.quit()

