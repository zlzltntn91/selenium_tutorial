import time
import random

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_helper import SeleniumHelper
from selenium.webdriver.common.by import By

dept = '4880155'
url = "http://localhost:8080"

helper = SeleniumHelper(url)
helper.login()

helper.get('/mng/cnt/contractBusiList')
helper.driver.execute_script('getAddForm()')

# 담당자정보 등록
helper.wait_and_click(By.CSS_SELECTOR, '#searchUser')
time.sleep(1)

helper.wait_and_click(By.CSS_SELECTOR, f'.openUser span[data-dept-id="{dept}"]')
time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, '.openUser tbody tr td:nth-child(1)')
time.sleep(1)

# 발주부서 등록
helper.wait_and_click(By.CSS_SELECTOR, '#searchDept')
time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, f'.openDepartment span[data-dept-id="{dept}"]')
time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, '.openDepartment tbody tr td:nth-child(1)')
time.sleep(1)

# 발주부서 등록
helper.wait_and_click(By.CSS_SELECTOR, '#searchMngTrgt')
time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, f'.openMgtarget span[data-dept-id="{dept}"]')
time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, '.openMgtarget tbody tr td:nth-child(1)')
time.sleep(1)


timestamp = str(int(time.time()))
title = f"테스트도급사업_{timestamp}"
# 계약명 입력
helper.wait_and_send_keys(By.NAME, "mngTrgt.mngTrgtNm", title)

select_elems = helper.driver.find_elements(By.TAG_NAME, 'select')
for select_elem in select_elems:
    select = Select(select_elem)
    valid_options = [opt for opt in select.options if opt.get_attribute('value') != '']
    if valid_options:
        rand_opt = random.choice(valid_options)
        select.select_by_value(rand_opt.get_attribute('value'))
        time.sleep(1)

# helper.wait_and_send_keys(By.ID, "mngFclt.zip", f"{timestamp}")
# helper.wait_and_send_keys(By.ID, "mngFclt.addr", f"테스트주소_{timestamp}")

# 준공일 입력 (오늘 날짜)
today = time.strftime("%Y-%m-%d")

# 전화번호
helper.wait_and_send_keys(By.NAME, "contBiz.telno", f"{timestamp}")
# 계약대상명 입력
helper.wait_and_send_keys(By.NAME, "contBiz.ctrtTrprNm", f"계약대상명 {timestamp}")
# 계약금액
helper.wait_and_send_keys(By.NAME, "contBiz.ctrtAmt", f"{timestamp}")
# 수행업무
helper.wait_and_send_keys(By.NAME, "contBiz.flfmtTask", f"수행업무 {timestamp}")
# 재해유형
checkbox = helper.driver.find_element(By.NAME, "contBiz.disasterTy").click()

# 상위사업장명(검색 버튼 클릭)
# helper.wait_and_click(By.ID, "searchMngTrgt")
# time.sleep(1)
# helper.wait_and_click(By.CSS_SELECTOR, "#pop-content > div.pop-code-content > div.pop-code-box > div > div.pop-screen-wrap > div.pop-screen-wrap-left > div > ul > li > ul > li:nth-child(1) > span")

# 화재예방보험 시작/종료일 (어제 날짜)
yesterday = (time.localtime(time.time() - 86400))
yesterday = time.strftime("%Y-%m-%d", yesterday)
helper.wait_and_send_keys(By.NAME, "contBiz.ctrtBgngDt", yesterday)
helper.wait_and_send_keys(By.NAME, "contBiz.ctrtEndDt", today)

# 안전관계자 등록
helper.wait_and_click(By.CSS_SELECTOR, '#searchMngUser')
helper.wait_and_click(By.CSS_SELECTOR, f'.openOfficial span[data-dept-id="{dept}"]')
helper.wait_and_select_by_value(By.NAME, 'batchObl', 'CMM6000001')
helper.wait_and_select_by_value(By.NAME, 'picTy', 'CMM7000001')
helper.wait_and_select_by_value(By.NAME, 'jbttl', 'CMM5000002')

max_wait = 10  # 최대 10초 대기
for i in range(max_wait):
    trs = helper.driver.find_elements(By.CSS_SELECTOR, 'tbody[id="sourceBody"] > tr')
    if len(trs) > 1:
        # print(f"tr 개수: {len(trs)}개 - 생성됨")
        break
    time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, 'input[name="sourceChkListAll"]')
helper.wait_and_click(By.CSS_SELECTOR, '#sourceForm > div > div > div > div > div.total-wrap.mg_b10 > div.total-btn-wrap > button')

helper.driver.execute_script('btnMngUserSave();')
time.sleep(1)

# 수탁정보 등록
for i in range(10):
    helper.wait_and_click(By.CSS_SELECTOR, '#contTrusteesAdd')
    # 수탁정보 입력값 자동화
    time.sleep(0.5)
    ran = random.randint(1, 9)
    helper.driver.find_element(By.ID, 'contTrustees.trusteeNm').send_keys(f'테스트업체 {timestamp}')
    helper.driver.find_element(By.ID, 'contTrustees.tpbiz').send_keys(f'제조업 {timestamp}')
    helper.driver.find_element(By.ID, 'contTrustees.brno').send_keys(f'1{ran}3-{i}5-{ran}{ran}8{ran}0')
    helper.driver.find_element(By.ID, 'contTrustees.trustee').send_keys(helper.random_korean_name())
    helper.driver.find_element(By.ID, 'contTrustees.telno').send_keys(f'010-{ran}{i}{ran}4-{ran}6{i}8')
    helper.driver.find_element(By.ID, 'contTrustees.permntWrkrCnt').send_keys(random.randint(1, 100))
    permanent_cnt = int(helper.driver.find_element(By.ID, 'contTrustees.permntWrkrCnt').get_attribute("value") or 1)
    helper.driver.find_element(By.ID, 'contTrustees.prtpntCnt').send_keys(random.randint(permanent_cnt, 100))
    helper.driver.execute_script('addTrustee();')

helper.driver.execute_script('sendForm();')
# 사업장 등록 완료 후, 사업장 목록으로 redirect

# 사업장 조회
helper.wait_and_click(By.CSS_SELECTOR, '#searchForm > div:nth-child(5) > div > div > div > div.board-type01 > table > tbody > tr > td.text-left.pd_l15 > a > span')

# element가 텍스트를 가질 때까지 대기
wait = WebDriverWait(helper.driver, 10)
element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1')))
text = element.text
if text == title:
    print("도급사업 등록 성공:", text)
    helper.quit()
else:
    print("도급사업 등록 실패:", text)
