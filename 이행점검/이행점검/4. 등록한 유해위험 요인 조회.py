import time
from selenium_helper import SeleniumHelper
from selenium.webdriver.common.by import By

url = "http://localhost:8080"
helper = SeleniumHelper(url)
helper.login()

helper.get('/chk/imp/ImplementList')
selectRowNum = 3
helper.wait_and_click(By.CSS_SELECTOR, f'#searchForm table tbody tr:nth-child({selectRowNum}) td:nth-child(2)')

# 안전보건관계자 선택
helper.wait_and_click(By.CSS_SELECTOR, '#implChckTable > tbody > tr:nth-child(1)')
time.sleep(1)

trIndex = 1
helper.wait_and_click(By.CSS_SELECTOR, f'#hazardTable tbody tr:nth-child({trIndex})')
tr_elem = helper.driver.find_element(By.CSS_SELECTOR, f"#hazardTable tbody tr:nth-child({trIndex}) td div")
data_obj = tr_elem.get_attribute("data-hazard-id")

logs = helper.driver.get_log("browser")
hazardId = logs[-1]["message"] if logs else None

if hazardId and data_obj in hazardId:
    print("디비에 저장된 유해위험요인")
    # tr_elem.click()
else:
    print("신규 유해위험요인")
    # tr_elem.click()

helper.quit()
