import time
from selenium import webdriver

#Copy the chromedriver
openChrome = webdriver.Chrome(
    executable_path="c:\Program Files (x86)\Google\Chrome\chromedriver.exe")

openChrome.maximize_window()
# web URL
openChrome.get("https://github.com/login")
# Wait for sometime till page is loaded
time.sleep(3)
# Set your username and password for login
username = "your username here"
password = "your password here"

# Entering the username in the username Field 
usernameField = openChrome.find_element_by_name("login")
usernameField.send_keys(username)
time.sleep(2)

usernameField = openChrome.find_element_by_name("password")
usernameField.send_keys(password)
time.sleep(2)

# Finding the login button of github by name
loginButton = openChrome.find_element_by_name("commit")
loginButton.click()

print("\nLogged-In Successfully")
