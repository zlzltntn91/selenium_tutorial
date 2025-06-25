import time
from selenium_helper import SeleniumHelper
from selenium.webdriver.common.by import By

timeStamp = time.strftime("H%M%S")
url = "http://localhost:8080"
helper = SeleniumHelper(url)
helper.login()

helper.get('/chk/imp/ImplementList')

time.sleep(1)
selectRowNum = 3
helper.wait_and_click(By.CSS_SELECTOR, f'#searchForm table tbody tr:nth-child({selectRowNum}) td:nth-child(2)')

helper.wait_and_click(By.CSS_SELECTOR, '#implChckTable > tbody > tr:nth-child(1)')
helper.wait_and_click(By.CSS_SELECTOR, '#regHazard')

# 디버깅: 현재 select id 출력
selects = helper.driver.find_elements(By.TAG_NAME, "select")
for s in selects:
    print("select id:", s.get_attribute("id"))
helper.wait_and_select_by_value(By.ID, "hazardTy", "CMM8000002")  # 분류
helper.wait_and_select_by_value(By.ID, "prgrsStts", "CHK1100001") # 진행상태
# 장소(작업명)
helper.wait_and_send_keys(By.ID, "jobNm", f"테스트 작업장 {timeStamp}")

# 원인
helper.wait_and_send_keys(By.ID, "hazardCause", f"테스트 원인 {timeStamp}")

# 유해위험요인
helper.wait_and_send_keys(By.ID, "hazardCn", f"테스트 유해위험요인 내용 {timeStamp}")

# 현재 안전보건조치
helper.wait_and_send_keys(By.ID, "curntActn", f"테스트 안전보건조치 {timeStamp}")

# 현재 위험성 - 가능성(빈도)
helper.wait_and_send_keys(By.ID, "curntPssible", "3")

# 현재 위험성 - 중대성(강도)
helper.wait_and_send_keys(By.ID, "cumtImpormt", "2")

# 현재 위험성 - 위험성
helper.wait_and_send_keys(By.ID, "curntRisk", "1")

# 법적근거
for i in range(1, 4):
    helper.wait_and_click(By.ID, "btnAddHzd")
    xpath = f'//*[@id="sourceInnerContents"]/tr[{i}]/td[1]/button'
    helper.wait_and_click_xpath(xpath)

helper.driver.execute_script('saveHazard()')

helper.quit()
