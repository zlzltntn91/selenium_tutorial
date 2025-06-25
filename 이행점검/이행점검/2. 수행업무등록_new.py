import time
from time import sleep

from selenium_helper import SeleniumHelper
from selenium.webdriver.common.by import By

url = "http://localhost:8080"
helper = SeleniumHelper(url)
helper.login()

helper.get('/chk/imp/ImplementList')

selectRowNum = 4
helper.wait_and_click(By.CSS_SELECTOR, f'#searchForm table tbody tr:nth-child({selectRowNum}) td:nth-child(2)')

# 안전보건관계자 선택
rows = helper.driver.find_elements(By.CSS_SELECTOR, '#implChckTable > tbody > tr')
for idx, row in enumerate(rows, start=1):
    helper.wait_and_click(By.CSS_SELECTOR, f'#implChckTable > tbody > tr:nth-child({idx})')

    time.sleep(1)
    helper.driver.execute_script('taskModifyView();')

    timeStamp = time.strftime("%Y%m%d%H%M%S")
    # 팝업 입력 자동화 (수행업무 등록)
    # 점검예정일자
    helper.wait_and_send_keys(By.NAME, 'chckPrnmntDt', '2025-07-01')
    # 점검일자(시작, 종료)
    helper.wait_and_send_keys(By.NAME, 'chckBgngDt', '2025-07-01')
    helper.wait_and_send_keys(By.NAME, 'chckEndDt', '2025-07-10')
    # 진행상태
    helper.wait_and_select_by_value(By.NAME, 'cprgrsStts', '01')
    # 점검내용
    helper.wait_and_send_keys(By.ID, 'chckCn', f'자동화 점검내용 입력 {timeStamp}')
    # 개선내용
    helper.wait_and_send_keys(By.ID, 'imprvCn', f'자동화 개선내용 입력 {timeStamp}')
    helper.wait_and_send_keys(By.ID, "wpsInCn", "1")
    helper.wait_and_send_keys(By.ID, "wpsImprvCn", "2")
    helper.wait_and_send_keys(By.ID, "swpInCn", "3")
    helper.wait_and_send_keys(By.ID, "swpImprvCn", "4")

    # 유해위험요인 등록
    for i in range(3):
        helper.wait_and_click(By.CSS_SELECTOR, '#regHazard')

        # 디버깅: 현재 select id 출력
        selects = helper.driver.find_elements(By.TAG_NAME, "select")
        for s in selects:
            print("select id:", s.get_attribute("id"))
        helper.wait_and_select_by_value(By.ID, "hazardTy", "CMM8000002")  # '전기적 요인'

        timeStamp = time.strftime("%H%M%S")

        # 장소(작업명)
        helper.wait_and_send_keys(By.ID, "jobNm", f"테스트 작업장 {timeStamp}")

        # 분류
        helper.wait_and_select_by_value(By.ID, "prgrsStts", "CHK1100002")

        # 원인
        helper.wait_and_send_keys(By.ID, "hazardCause", f"테스트 원인 {timeStamp}")

        # 유해위험요인
        helper.wait_and_send_keys(By.ID, "hazardCn", f"테스트 유해위험요인 내용 {timeStamp}")

        # 현재 안전보건조치
        helper.wait_and_send_keys(By.ID, "curntActn", f"테스트 안전보건조치 {timeStamp}")

        # 현재 위험성 - 가능성(빈도)
        helper.driver.find_element(By.ID, "curntPssible").send_keys("3")

        # 현재 위험성 - 중대성(강도)
        helper.driver.find_element(By.ID, "cumtImpormt").send_keys("2")

        # 현재 위험성 - 위험성
        helper.driver.find_element(By.ID, "curntRisk").send_keys("2")

        # # 법적근거
        # for i in range(1, 4):
        #     helper.wait_and_click(By.ID, "btnAddHzd")
        #     xpath = f'//*[@id="sourceInnerContents"]/tr[{i}]/td[1]/button'
        #     helper.wait_and_click_xpath(xpath)

        helper.driver.execute_script('saveHazard()')

    helper.wait_and_click(By.CSS_SELECTOR,
                          '#pop-content > div.pop-code-btn > div > button.btn-black.pop-custom-btn.waves-effect.waves-light.popclosed-layer')
    time.sleep(1)
    helper.wait_and_click(By.CSS_SELECTOR,
                          '#pop-content > div.pop-code-btn > div > button.btn-gray.pop-custom-btn.waves-effect.waves-light.popclosed-layer.custom-close')


helper.quit()


