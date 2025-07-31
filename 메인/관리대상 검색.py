import time

from selenium.webdriver import Keys

from selenium_helper import SeleniumHelper
from selenium.webdriver.common.by import By

url = "http://localhost:8080"
helper = SeleniumHelper(url)
helper.login()


helper.get('/main')
helper.wait_and_select_by_value(By.CSS_SELECTOR, '#mainSearchTarget', '3000000')
helper.wait_and_send_keys(By.CSS_SELECTOR, 'input[name="searchKeyword"]', '테스트')
helper.driver.find_element(By.CSS_SELECTOR, 'input[name="searchKeyword"]').send_keys(Keys.ENTER)

# helper.quit()
