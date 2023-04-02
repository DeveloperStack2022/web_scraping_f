import requests
import random

from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from credentials import username, password


class FaceBookBot():

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(options=options)

    def login(self, username, password):
        self.driver.get("https://www.facebook.com/login")

        sleep(2)

        email_in = self.driver.find_element('xpath', '//*[@id="email"]')
        email_in.send_keys(username)

        password_in = self.driver.find_element('xpath', '//*[@id="pass"]')
        password_in.send_keys(password)

        login_btn = self.driver.find_element('xpath', '//*[@id="loginbutton"]')
        login_btn.click()

        sleep(2)

    def log_in_basic(self):
        POST_LOGIN_URL = 'https://mbasic.facebook.com/login'

        payload = {
            'email': username,
            'pass': password
        }

        with requests.Session() as session:
            post = session.post(POST_LOGIN_URL, data=payload)

    def post_likes(self):
        # This URL will be the URL that your login form points to with the "action" tag.
        POST_LOGIN_URL = 'https://mbasic.facebook.com/login'

        # This URL is the page you actually want to pull down with requests.
        post_ID = 'the-post-ID'
        limit = 200
        REQUEST_URL = f'https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit={limit}&total_count=17&ft_ent_identifier={post_ID}'

        payload = {
            'email': username,
            'pass': password
        }

        with requests.Session() as session:
            post = session.post(POST_LOGIN_URL, data=payload)
            r = session.get(REQUEST_URL)
        soup = BeautifulSoup(r.content, "html.parser")
        names = soup.find_all('h3', class_='be')
        people_who_liked = []
        for name in names:
            people_who_liked.append(name.text)

        return people_who_liked

    def post_shares(self):
        # This URL will be the URL that your login form points to with the "action" tag.
        POST_LOGIN_URL = 'https://mbasic.facebook.com/login'

        post_ID = 'the-post-ID'
        # This URL is the page you actually want to pull down with requests.
        REQUEST_URL = f'https://m.facebook.com/browse/shares?id={post_ID}'

        payload = {
            'email': username,
            'pass': password
        }

        with requests.Session() as session:
            post = session.post(POST_LOGIN_URL, data=payload)
            r = session.get(REQUEST_URL)
        soup = BeautifulSoup(r.content, "html.parser")
        names = soup.find_all('span')
        people_who_shared = []
        for name in names:
            people_who_shared.append(name.text)

        return people_who_shared

    def page_likes(self):
        self.login(username, password)

        photo_id = "5607443702684195"
        # # This URL is the page you actually want to pull down with requests.
        REQUEST_URL = f'https://www.facebook.com/photo/?fbid={photo_id}&set=a.106023242826296'
        # https://www.facebook.com/photo/?fbid=4041415652587892&set=a.106023242826296
        # https://www.facebook.com/photo/?fbid=4041415652587892&set=a.106083829454447
        self.driver.get(REQUEST_URL)
        # self.driver.find_element
        # sleep(2)
        #  //span[@id="ssrb_root_start"]
        # //div[@class="x6s0dn4 x78zum5 x1iyjqo2 x6ikm8r x10wlt62"]
        # div_emotion = self.driver.find_element(
        # 'xpath', 'div[@class="x6s0dn4 x78zum5 x1iyjqo2 x6ikm8r x10wlt62"]')
        # emotion_likes = self.driver.find_element(
        #     'xpath', '//*[@id="ssrb_root_start"]')
        # div_emotion.click()

        # for i in range(1, 15):
        #     self.driver.execute_script(
        #         "window.scrollTo(0, document.body.scrollHeight);")
        #     sleep(3)

        # page = self.driver.page_source
        # soup = BeautifulSoup(page, "html.parser")
        # print(soup)

        sleep(2)
        div_role_ = self.driver.find_element(
            'xpath', '//span[@class=" xrbpyxo x6ikm8r x10wlt62 xlyipyv x1exxlbk"]')
        sleep(2)
        div_role_.click()
        sleep(2)
        # class="x78zum5 x1iyjqo2 x1n2onr6 xdt5ytf"
        div_likes_friends_ = self.driver.find_element(
            'xpath', """//div[2][@class="x78zum5 x1iyjqo2 x1n2onr6 xdt5ytf"]""")
        self.driver.execute(
            "arguments[0].scrollIntoView(scrollIntoView({ behavior: 'smooth', block: 'end', inline: 'end' });", div_likes_friends_)

        sleep(200)
        # people_who_liked_page = []
        # for name in names:
        #     people_who_liked_page.append(name.text)

        # return people_who_liked_page

    def select_winner(self, list_A, list_B, list_C):
        eligible_to_win = []
        for name in list_A:
            if name in list_B and name in list_C:
                eligible_to_win.append(name)
        return eligible_to_win


bot = FaceBookBot()
people_who_follow = bot.page_likes()
# people_who_liked = bot.post_likes()
# people_who_shared = bot.post_shares()

# eligible = bot.select_winner(
#     people_who_liked, people_who_follow, people_who_shared)
# winner = random.choice(eligible)
# print(winner)
