

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_helper import SeleniumHelper
from selenium.webdriver.common.by import By

url = "http://localhost:8080"
helper = SeleniumHelper(url)
helper.login()

helper.get('/chk/imp/ImplementList')

selectRowNum = 1
helper.wait_and_click(By.CSS_SELECTOR, f'#searchForm table tbody tr:nth-child({selectRowNum}) td:nth-child(2)')

# WebDriverWait 객체 생성 (최대 10초 대기)
wait = WebDriverWait(helper.driver, 10)

# 안전보건관계자 선택
rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#implChckTable > tbody > tr')))
for idx, row in enumerate(rows, start=1):
    helper.wait_and_click(By.CSS_SELECTOR, f'#implChckTable > tbody > tr:nth-child({idx})')

    hazards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#hazardTable > tbody > tr')))
    for i in range(1, len(hazards) + 1):
        helper.wait_and_click(By.CSS_SELECTOR, f'#hazardTable > tbody > tr:nth-child({i})')
        time.sleep(10)

    time.sleep(1)
    # helper.driver.execute_script('taskModifyView();')

helper.quit()

