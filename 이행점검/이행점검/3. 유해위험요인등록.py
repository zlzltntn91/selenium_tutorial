from selenium_helper import SeleniumHelper
from selenium.webdriver.common.by import By

helper = SeleniumHelper()
helper.login()

helper.driver.get('http://localhost:8080/chk/imp/ImplementList')
helper.wait_and_click(By.CSS_SELECTOR, '#searchForm >  tbody > tr:nth-child(1) > td.text-left.pd_l15 ')

helper.wait_and_click(By.CSS_SELECTOR, '#implChckTable > tbody > tr:nth-child(1)')
helper.wait_and_click(By.CSS_SELECTOR, '#regHazard')

# 디버깅: 현재 select id 출력
selects = helper.driver.find_elements(By.TAG_NAME, "select")
for s in selects:
    print("select id:", s.get_attribute("id"))
helper.wait_and_select_by_value(By.ID, "hazardTy", "CMM8000002")  # '전기적 요인'

# 장소(작업명)
helper.wait_and_send_keys(By.ID, "jobNm", "테스트 작업장")

# 분류
helper.wait_and_select_by_value(By.ID, "prgrsStts", "CHK1100002")

# 원인
helper.wait_and_send_keys(By.ID, "hazardCause", "테스트 원인")

# 유해위험요인
helper.wait_and_send_keys(By.ID, "hazardCn", "테스트 유해위험요인 내용")

# 현재 안전보건조치
helper.wait_and_send_keys(By.ID, "curntActn", "테스트 안전보건조치")

# 현재 위험성 - 가능성(빈도)
helper.driver.find_element(By.ID, "curntPssible").send_keys("3")

# 현재 위험성 - 중대성(강도)
helper.driver.find_element(By.ID, "cumtImpormt").send_keys("2")

# 현재 위험성 - 위험성
helper.driver.find_element(By.ID, "curntRisk").send_keys("2")

# 법적근거
for i in range(1, 4):
    helper.wait_and_click(By.ID, "btnAddHzd")
    xpath = f'//*[@id="sourceInnerContents"]/tr[{i}]/td[1]/button'
    helper.wait_and_click_xpath(xpath)

helper.driver.execute_script('saveHazard()')

helper.quit()
