
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--window-position=200,400")
options.add_argument("--window-size=1200,1200")  # 브라우저 크기 설정
options.add_experimental_option('detach', True)  # 브라우저 자동 닫힘 방지
driver = webdriver.Chrome(options=options)

driver.get('http://localhost:8080')
driver.implicitly_wait(10)
driver.execute_script("document.body.style.zoom='100%'")
driver.find_element(By.ID, 'openSignup').click()


import uuid
user_uuid = str(uuid.uuid4())[:10].replace('-', '')
# 각 input에 값 입력
driver.find_element(By.ID, 'loginId').send_keys(user_uuid)
driver.find_element(By.ID, 'userNm').send_keys(user_uuid)

driver.find_element(By.ID, 'searchDept').click()
driver.implicitly_wait(3)
assert driver.find_element(By.ID, 'signUpForm').is_displayed()

driver.find_element(By.CSS_SELECTOR, '[data-dept-id="4880155"]').click()
driver.implicitly_wait(3)
assert driver.find_element(By.CSS_SELECTOR, '#sourceInnerContents tbody tr').is_displayed()
driver.find_element(By.CSS_SELECTOR, '#sourceInnerContents > table > tbody > tr > td:nth-child(1) > button').click()


driver.find_element(By.ID, 'userEml').send_keys('test@example.com')
driver.find_element(By.ID, 'userPswd').send_keys('qwer1234!')
driver.find_element(By.ID, 'userPswdCk').send_keys('qwer1234!')
driver.find_element(By.ID, 'mobileno').send_keys('01012345678')

# 약관동의 체크박스 클릭
driver.find_element(By.ID, 'trmsAgreYn').click()
driver.find_element(By.ID, 'prvcClctAgreYn').click()
button = driver.find_element(By.CSS_SELECTOR, 'button.btn-black.pop-custom-btn.waves-effect.waves-light').click()
button = driver.find_element(By.CSS_SELECTOR, '.btn.btnBlue').click()


driver.quit()
driver = webdriver.Chrome(options=options)
driver.get('http://localhost:8080')
driver.implicitly_wait(10)

driver.execute_script("document.body.style.zoom='100%'")
driver.find_element(By.ID, 'username').send_keys(user_uuid)
driver.find_element(By.ID, 'password').send_keys('qwer1234!')
driver.find_element(By.ID, 'password').send_keys(Keys.ENTER)





