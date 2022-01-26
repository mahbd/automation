import json
import time
import os

from selenium import webdriver

try:
    from secret import MESSENGER_EMAIL, MESSENGER_PASSWORD
except ImportError:
    print("Failed to import secret. Please create one")
    exit(1)

browser = webdriver.Chrome()
cookies = [{}]


def generate_cookies():
    global cookies
    browser.get('https://messenger.com/')
    time.sleep(5)
    email_box = browser.find_element_by_id("email")
    email_box.send_keys(MESSENGER_EMAIL)
    password_box = browser.find_element_by_id("pass")
    password_box.send_keys(MESSENGER_PASSWORD)

    time.sleep(10)

    login_button = browser.find_element_by_id("loginbutton")
    login_button.click()
    time.sleep(10)
    cookies = browser.get_cookies()
    if type(cookies) != dict:
        string = json.dumps(cookies)
        with open('../messenger_cookie.json', 'w+') as file:
            file.write(string)
    else:
        print(cookies)
try:
    with open('../messenger_cookie.json', 'r') as file:
        text = file.read()
        try:
            cookies = json.loads(text)
        except json.JSONDecodeError:
            pass
except FileNotFoundError:
    generate_cookies()

# check if cookies is empty
if len(cookies) == 0:
    generate_cookies()


def send_message(message: str, repeat=1):
    global cookies
    browser.get('https://messenger.com/')
    for cookie in cookies:
        browser.add_cookie(cookie_dict=cookie)
    browser.get('https://www.messenger.com/t/100028306997168/')
    time.sleep(2)
    message_box = browser.find_element_by_xpath('//div[@role="textbox"]')
    while repeat > 0:
        message_box.send_keys(message)
        time.sleep(0.1)
        message_box.send_keys('\n')
        repeat -= 1


send_message("Test message 1", 10)
