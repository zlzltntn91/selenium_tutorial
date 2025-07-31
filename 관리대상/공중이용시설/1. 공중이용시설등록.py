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


helper.get('/mng/fat/facilitiesList')
helper.driver.execute_script('getAddForm()')

# 담당자정보 등록
helper.wait_and_click(By.CSS_SELECTOR, '#searchUser')
time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, f'.openUser span[data-dept-id="{dept}"]')
time.sleep(1)
helper.wait_and_click(By.CSS_SELECTOR, '.openUser tbody tr td:nth-child(1)')
time.sleep(1)


timestamp = str(int(time.time()))
title = f"테스트공중이용시설_{timestamp}"
# 시설명 입력
helper.wait_and_send_keys(By.NAME, "mngTrgt.mngTrgtNm", title)

# 시설물 구분
# select_elem = helper.driver.find_element(By.CSS_SELECTOR, 'select[name="mngFclt.tpbizClsfCd"]')
# select = Select(select_elem)
# options = select.options
# rand_idx = random.randint(0, len(options) - 1)
# select.select_by_index(rand_idx)


select_elems = helper.driver.find_elements(By.TAG_NAME, 'select')
for select_elem in select_elems:
    select = Select(select_elem)
    valid_options = [opt for opt in select.options if opt.get_attribute('value') != '']
    if valid_options:
        rand_opt = random.choice(valid_options)
        select.select_by_value(rand_opt.get_attribute('value'))
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

# 시설물번호, 시설물세부번호 입력 (타임스탬프 사용)
helper.wait_and_send_keys(By.NAME, "mngFclt.fmsFcltNo", f"{timestamp}")
helper.wait_and_send_keys(By.NAME, "mngFclt.semiFcltNo", f"{timestamp}")

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
helper.wait_and_click(By.CSS_SELECTOR, '#tx01')

# 기타 내용 입력
# helper.wait_and_send_keys(By.ID, "mngFclt.etcCn", f"기타내용_{timestamp}")


helper.wait_and_send_keys(By.ID, "fcltScale.scale1", str(random.randint(100, 10000)))
helper.wait_and_send_keys(By.ID, "fcltScale.scale2", str(random.randint(10, 1000)))
helper.wait_and_send_keys(By.ID, "fcltScale.scale3", str(random.randint(1, 100)))
helper.wait_and_send_keys(By.ID, "fcltScale.scale4", str(random.randint(1, 10)))
helper.wait_and_send_keys(By.ID, "fcltScale.scale5", str(random.randint(10, 100)))
helper.wait_and_send_keys(By.ID, "fcltScale.scale6", str(random.randint(10, 1000)))
helper.wait_and_send_keys(By.ID, "fcltScale.scale7", str(random.randint(1, 10)))
helper.wait_and_send_keys(By.ID, "fcltScale.scale8", str(random.randint(10, 100)))
helper.wait_and_send_keys(By.ID, "fcltScale.scale9", str(random.randint(10, 1000)))
helper.wait_and_send_keys(By.ID, "fcltScale.scale10", str(random.randint(1, 5)))
helper.wait_and_send_keys(By.ID, "fcltScale.scale11", str(random.randint(1, 20)))
helper.wait_and_send_keys(By.ID, "fcltScale.scale12", str(random.randint(1, 500)))

# 안전관계자 등록
helper.wait_and_click(By.CSS_SELECTOR, '#searchMngUser')
helper.wait_and_click(By.CSS_SELECTOR, f'.openOfficial span[data-dept-id="{dept}"]')
helper.wait_and_select_by_value(By.NAME, 'batchObl', 'CMM6000001')
helper.wait_and_select_by_value(By.NAME, 'picTy', 'CMM7000001')
helper.wait_and_select_by_value(By.NAME, 'jbttl', 'CMM5000003')


max_wait = 10  # 최대 10초 대기
for i in range(max_wait):
    trs = helper.driver.find_elements(By.CSS_SELECTOR, 'tbody[id="sourceBody"] > tr')
    if len(trs) > 0:
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
helper.wait_and_click(By.CSS_SELECTOR, '#searchForm > div:nth-child(5) > div > div > div > div.board-type01 > table > tbody > tr > td.text-left.pd_l15 > a > span')

helper.quit()

# element가 텍스트를 가질 때까지 대기
wait = WebDriverWait(helper.driver, 2)
element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1')))
text = element.text
if text == title:
    print("공중이용시설 등록 성공:", text)
    helper.quit()
else:
    print("공중이용시설 등록 실패:", text)
