from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from auth_data import username, password
import time
import random


class InstagramBot():
    s = Service('./chromedriver/chromedriver')
    browser = webdriver.Chrome(service=s)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        s = Service('./chromedriver/chromedriver')
        self.browser = webdriver.Chrome(service=s)

    def kill_browser(self):
        self.browser.close()
        self.browser.quit()

    def login(self):
        browser = self.browser
        try:
            browser.get('https://www.instagram.com/')
            time.sleep(random.randrange(3, 5))

            username_input = browser.find_element(by=By.NAME, value="username")
            username_input.clear()
            username_input.send_keys(self.username)

            time.sleep(random.randrange(1, 2))

            password_input = browser.find_element(by=By.NAME, value="password")
            password_input.clear()
            password_input.send_keys(self.password)

            password_input.send_keys(Keys.ENTER)
            time.sleep(10)

            self.kill_browser()
        except Exception as ex:
            print(ex)
            self.kill_browser()

    def like_photos_by_hashtag(self, hashtag):
        browser = self.browser
        try:
            browser.get('https://www.instagram.com/')
            time.sleep(random.randrange(3, 5))

            username_input = browser.find_element(by=By.NAME, value="username")
            username_input.clear()
            username_input.send_keys(self.username)

            time.sleep(random.randrange(1, 2))

            password_input = browser.find_element(By.NAME, "password")
            password_input.clear()
            password_input.send_keys(self.password)

            password_input.send_keys(Keys.ENTER)
            time.sleep(random.randrange(5, 6))

            try:
                browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
                time.sleep(2)

                for i in range(1, 4):
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(random.randrange(3, 5))

                hrefs = browser.find_elements(By.TAG_NAME, 'a')

                posts_urls = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute('href')]

                for url in posts_urls:
                    try:
                        browser.get(url)
                        time.sleep(2)
                        like_button = browser.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()
                        time.sleep(random.randrange(85, 100))
                    except Exception as ex:
                        print(ex)

                self.kill_browser()
            except Exception as ex:
                print(ex)
                self.kill_browser()
        except Exception as ex:
            print(ex)
            self.kill_browser()

    def xpath_exists(self, url):
        browser = self.browser
        try:
            browser.find_element(By.XPATH, url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def like_exactly_post(self, userpost):
        browser = self.browser
        browser.get(userpost)
        time.sleep(4)


i = InstagramBot(username, password)
i.like_photos_by_hashtag('surfing')
