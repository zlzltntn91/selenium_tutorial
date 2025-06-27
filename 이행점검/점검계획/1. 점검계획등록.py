import time

from selenium.webdriver.common.by import By
import selenium.common.exceptions

from selenium_helper import SeleniumHelper

helper = SeleniumHelper()
helper.login()
timestamp = time.strftime("H%M%S")

helper.driver.get('http://localhost:8080/chk/pln/checkPlanList')
helper.driver.execute_script("getAddForm();")
time.sleep(1)

helper.wait_and_click(By.ID, 'plansBtn')
time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, '#pop-content > div.pop-code-content > div.pop-code-box > div > div > div > div > div > div.board-type03 > table > tbody > tr:nth-child(1) > td:nth-child(1) > button')
time.sleep(1)


helper.wait_and_send_keys(By.NAME, 'chckPlanNm', '테스트 점검계획명 ' + timestamp)
helper.wait_and_select_by_value(By.NAME, 'prslRng', 'CMM2000001')
helper.wait_and_select_by_value(By.NAME, 'chckTy', 'CMM1000001')
helper.wait_and_select_by_value(By.NAME, 'autoRegYn', 'Y')
helper.wait_and_send_keys(By.NAME, 'cn', '테스트 점검계획 내용 ' + timestamp)

helper.wait_and_click(By.ID, 'regMngTrgt')
#
helper.wait_and_click(By.CSS_SELECTOR, 'span[data-dept-id="4880155"]')
## tbody > name = sourceBody 안에 tr 이 생길 때까지 대기 또는 반복

max_wait = 10  # 최대 10초 대기
for i in range(max_wait):
    trs = helper.driver.find_elements(By.CSS_SELECTOR, 'tbody[id="sourceBody"] > tr')
    if len(trs) > 1:
        print(f"tr 개수: {len(trs)}개 - 생성됨")

        break
    time.sleep(1)

helper.wait_and_click(By.CSS_SELECTOR, 'input[name="sourceChkListAll"]')
helper.wait_and_click(By.CSS_SELECTOR, '#pop-content > div.pop-code-content > div.pop-code-box > div > div.pop-screen-wrap > div.pop-screen-wrap-right > div:nth-child(2) > div > div > div > div.total-wrap.mg_b10 > div.total-btn-wrap > button:nth-child(2)')
helper.driver.execute_script("btnMngSave();")

# 파일 업로드 input 요소에 파일 경로 전달
# file_input = helper.driver.find_element(By.CSS_SELECTOR, 'input[id="file-input"]')
# file_input.send_keys('/Users/zlamstn/Downloads/스칼렛아르테 사전예약 양식.docx')
# time.sleep(5)

helper.driver.execute_script('sendForm();')
helper.quit()