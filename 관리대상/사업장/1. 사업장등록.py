import time
import random

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_helper import SeleniumHelper
from selenium.webdriver.common.by import By

dept = '4880145'
url = "http://localhost:8080"
helper = SeleniumHelper(url)
helper.login()


helper.get('/mng/wop/workplaceList')
helper.driver.execute_script('getAddForm()')

# 담당자정보 등록
helper.wait_and_click(By.CSS_SELECTOR, '#searchUser')
time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, f'.openUser span[data-dept-id="{dept}"]')
time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, '.openUser tbody tr td:nth-child(1)')
time.sleep(1)


timestamp = str(int(time.time()))
title = f"테스트사업장_{timestamp}"
# 사업장명 입력
helper.wait_and_send_keys(By.NAME, "mngTrgt.mngTrgtNm", title)

# 업종분류(검색 버튼 클릭)
helper.wait_and_click(By.ID, "searchKsic")
time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, "#pop-content > div.pop-code-content > div.pop-code-box > div > div.pop-screen-wrap > div.pop-screen-wrap-left > div > ul > li > ul > li:nth-child(1) > span")
helper.wait_and_click(By.CSS_SELECTOR, "#sourceInnerContents > table > tbody > tr > td:nth-child(1) > button")
time.sleep(1)

# 주소 입력
helper.wait_and_click(By.CSS_SELECTOR, "#searchAddr")
time.sleep(1)
helper.wait_and_send_keys(By.NAME, "addrNm", "소사" + Keys.ENTER)
helper.wait_and_click(By.CSS_SELECTOR, "#addrInnerContents > tr:nth-child(1) > td:nth-child(1) > button")
time.sleep(1)
helper.wait_and_send_keys(By.ID, "mngFclt.daddr", f"상세주소_{timestamp}")

# helper.wait_and_send_keys(By.ID, "mngFclt.zip", f"{timestamp}")
# helper.wait_and_send_keys(By.ID, "mngFclt.addr", f"테스트주소_{timestamp}")

# 준공일 입력 (오늘 날짜)
today = time.strftime("%Y-%m-%d")
helper.wait_and_send_keys(By.NAME, "mngFclt.cmcnDe", today)

# 상위사업장명(검색 버튼 클릭)
# helper.wait_and_click(By.ID, "searchMngTrgt")
# time.sleep(1)
# helper.wait_and_click(By.CSS_SELECTOR, "#pop-content > div.pop-code-content > div.pop-code-box > div > div.pop-screen-wrap > div.pop-screen-wrap-left > div > ul > li > ul > li:nth-child(1) > span")

# 화재예방보험 시작/종료일 (어제 날짜)
yesterday = (time.localtime(time.time() - 86400))
yesterday = time.strftime("%Y-%m-%d", yesterday)
helper.wait_and_send_keys(By.NAME, "mngFclt.fpiBgngDt", yesterday)
helper.wait_and_send_keys(By.NAME, "mngFclt.fpiEndDt", today)

# 관리형태 체크박스(직접관리 체크)
helper.wait_and_click(By.CSS_SELECTOR, '#tx001')

# 기타 내용 입력
# helper.wait_and_send_keys(By.ID, "mngFclt.etcCn", f"기타내용_{timestamp}")


################ 근무인원
for i in range(2, 8):
    helper.wait_and_click(By.CSS_SELECTOR, '#fcltWrkrsAdd')
    time.sleep(1)

    val1 = random.randint(1, 30)
    val2 = random.randint(val1, 30)

    helper.wait_and_select_by_value(By.CSS_SELECTOR, '#codes', f'MNG110000{i}')
    helper.wait_and_send_keys(
        By.CSS_SELECTOR,
        '#pop-content > div.pop-code-content > div.pop-code-box > div > div.board-type02 > table > tbody > tr:nth-child(2) > td > div > input',
        str(val1)
    )
    helper.wait_and_send_keys(
        By.CSS_SELECTOR,
        '#pop-content > div.pop-code-content > div.pop-code-box > div > div.board-type02 > table > tbody > tr:nth-child(3) > td > div > input',
        str(val2)
    )
    helper.driver.execute_script('addWorkrs();')
################ 근무인원 끝

############# 물품정보
for i in range(5):
    helper.wait_and_click(By.CSS_SELECTOR, '#fcltCmdtysAdd')
    time.sleep(0.5)

    val2 = random.randint(1, 100)
    val3 = random.randint(1, 3)

    helper.wait_and_select_by_value(By.CSS_SELECTOR, '#codes', f'MNG12{val3}0000')
    time.sleep(0.5)
    select_elem = helper.driver.find_element(By.CSS_SELECTOR, '#childrenCodes')
    select = Select(select_elem)
    options = select.options

    rand_idx = random.randint(0, len(options) - 1)
    select.select_by_index(rand_idx)

    helper.wait_and_send_keys(
        By.CSS_SELECTOR,
        '#pop-content > div.pop-code-content > div.pop-code-box > div > div.board-type02 > table > tbody > tr:nth-child(3) > td > div > input',
        str(val2)
    )
    helper.driver.execute_script('addCmdtys();')
################ 물품정보 끝

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

helper.driver.execute_script('sendForm();')
# 사업장 등록 완료 후, 사업장 목록으로 redirect

# 사업장 조회
helper.wait_and_click(By.CSS_SELECTOR, '#searchForm > div:nth-child(5) > div > div > div > div.board-type01 > table > tbody > tr:nth-child(1) > td.text-left.pd_l15')

# element가 텍스트를 가질 때까지 대기
wait = WebDriverWait(helper.driver, 10)
element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#sub-content > div.sub-code-content > div.sub-code-box > div:nth-child(4) > div.board-type02 > table > tbody > tr:nth-child(2) > td:nth-child(3) > div')))
text = element.text
if text == title:
    print("사업장 등록 성공:", text)
    helper.quit()
else:
    print("사업장 등록 실패:", text)
