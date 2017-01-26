import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class OpenTwitter(unittest.TestCase):

    userID = input("Email: ")
    passID = input("Pass: ")
    YourMessage = input("Your Message: ")

    def setUp(self):
       try:
           self.driver = webdriver.Firefox()
       except Exception as e:
           print(str(e))

    def test_search_in_python_org(self):
        try:
            driver = self.driver
            driver.get("https://twitter.com/")
            inputEmail = driver.find_element_by_id('signin-email')
            inputPass = driver.find_element_by_id('signin-password')
            button = driver.find_element_by_xpath("//button[contains(text(),'Log in')]")

            inputEmail.clear()
            inputPass.clear()

            inputEmail.send_keys(OpenTwitter.userID)
            inputPass.send_keys(OpenTwitter.passID)

            button.click()

            el = driver.find_element_by_id('tweet-box-home-timeline')
            el.send_keys(OpenTwitter.YourMessage)
            time.sleep(3)
            driver.find_element_by_xpath(
                "//button[@class='btn primary-btn tweet-action tweet-btn js-tweet-btn']").click()

            time.sleep(10)
        except Exception as e:
            print(str(e))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()