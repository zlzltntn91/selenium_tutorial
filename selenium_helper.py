from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class SeleniumHelper:
    def __init__(self):
        options = Options()
        options.add_experimental_option('detach', True)  # 브라우저 자동 닫힘 방지
        options.add_argument("--auto-open-devtools-for-tabs")
        options.add_argument("--window-size=2560,1440")
        self.driver = None
        for _ in range(10):
            try:
                self.driver = webdriver.Chrome(options=options)
                self.driver.get("http://localhost:8080")
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

    def login(self, username="ADMIN00000", password="qwer1234!"):
        self.driver.execute_script(f'document.querySelector("#username").value = "{username}"')
        self.driver.execute_script(f'document.querySelector("#password").value = "{password}"')
        self.driver.execute_script('document.querySelector("#remember").checked = true')
        self.driver.execute_script('login()')
        time.sleep(1)

    def wait_and_click(self, by, selector, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, selector))
        ).click()

    def wait_and_send_keys(self, by, selector, value, timeout=10):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, selector))
        )
        elem.clear()
        elem.send_keys(value)

    def wait_and_select_by_value(self, by, selector, value, timeout=10):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, selector))
        )
        Select(elem).select_by_value(value)

    def wait_and_click_xpath(self, xpath, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        ).click()

    def upload_file(self, by, selector, file_path, timeout=10):
        """
        파일 첨부 input에 파일 경로를 입력하여 업로드합니다.
        예: helper.upload_file(By.ID, "fileInput", "/Users/zlamstn/파일경로/파일명.txt")
        """
        elem = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, selector))
        )
        elem.send_keys(file_path)

    def quit(self):
        self.driver.quit()
