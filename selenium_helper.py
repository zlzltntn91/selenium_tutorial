import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time


class SeleniumHelper:
    def __init__(self, url="http://localhost:8080"):
        options = Options()
        options.add_experimental_option('detach', True)  # 브라우저 자동 닫힘 방지
        options.add_argument("--auto-open-devtools-for-tabs")
        options.add_argument("--window-size=2560,1440")
        # webdriver.Chrome()의 desired_capabilities는 deprecated, 대신 options에 capability 추가
        options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
        self.url = url
        self.driver = None
        for _ in range(10):
            try:
                self.driver = webdriver.Chrome(options=options)
                self.driver.get(url)
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
            except Exception as e:
                if self.driver is not None:
                    self.driver.quit()
                self.driver = None
                print(e)
            if self.driver is not None:
                if self.driver.title == 'SAFE':
                    break
                else:
                    self.driver.quit()

    def get(self, url):
        self.driver.get(self.url + url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def login(self, username="58727428b", password="0000"):
        self.wait_and_send_keys(By.ID, "username", username)
        self.wait_and_send_keys(By.ID, "password", password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "remember"))
        ).click()
        # self.driver.execute_script('login()')
        time.sleep(1)

        self.wait_and_click(By.CSS_SELECTOR, "button[type='submit']")

    def wait_and_click(self, by, selector, timeout=15):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, selector))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
        elem.click()

    def wait_and_send_keys(self, by, selector, value, timeout=15):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, selector))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
        elem.clear()
        elem.send_keys(value)

    def wait_and_select_by_value(self, by, selector, value, timeout=15):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, selector))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
        Select(elem).select_by_value(value)

    def wait_and_click_xpath(self, xpath, timeout=15):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
        elem.click()

    def upload_file(self, by, selector, file_path, timeout=15):
        """
        파일 첨부 input에 파일 경로를 입력하여 업로드합니다.
        예: helper.upload_file(By.ID, "fileInput", "/Users/zlamstn/파일경로/파일명.txt")
        """
        elem = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, selector))
        )
        elem.send_keys(file_path)

    def random_korean_name(self):
        last_names = ['김', '이', '박', '최', '정', '강', '조', '윤', '장', '임']
        first_names = ['민수', '서연', '지훈', '지민', '현우', '수빈', '예은', '도현', '시우', '하은']
        return random.choice(last_names) + random.choice(first_names)

    def quit(self):
        self.driver.quit()
