import time
from selenium_helper import SeleniumHelper
from selenium.webdriver.common.by import By

dept = '4880155'
helper = SeleniumHelper()
if helper.driver is None:
    exit()

helper.login()

idx = 3
helper.get('/chk/imp/ImplementList')
helper.wait_and_click(By.CSS_SELECTOR, f'#searchForm table tbody tr:nth-child({idx}) td:nth-child(2)')
helper.wait_and_click(By.CSS_SELECTOR, '#sub-content > div.sub-code-btn > div:nth-child(2) > button')

# 안전관계자 등록
helper.wait_and_click(By.CSS_SELECTOR, '#searchMngUser')
helper.wait_and_click(By.CSS_SELECTOR, f'span[data-dept-id="{dept}"]')
helper.wait_and_select_by_value(By.NAME, 'batchObl', 'CMM6000001')
helper.wait_and_select_by_value(By.NAME, 'picTy', 'CMM7000001')
helper.wait_and_select_by_value(By.NAME, 'jbttl', 'CMM5000002')
max_wait = 10  # 최대 10초 대기
for i in range(max_wait):
    trs = helper.driver.find_elements(By.CSS_SELECTOR, 'tbody[id="sourceBody"] > tr')
    if len(trs) > 1:
        print(f"tr 개수: {len(trs)}개 - 생성됨")
        break
    time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, 'input[name="sourceChkListAll"]')
helper.wait_and_click(By.CSS_SELECTOR, '#sourceForm > div > div > div > div > div.total-wrap.mg_b10 > div.total-btn-wrap > button')

helper.driver.execute_script('btnMngUserSave();')

helper.quit()
