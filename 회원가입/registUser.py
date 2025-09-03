
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# url = "http://100.11.1.244:8090"
url = "http://localhost:8080"

options = Options()
options.add_argument("--auto-open-devtools-for-tabs")
options.add_argument("--window-position=200,400")
options.add_argument("--window-size=1200,1200")  # 브라우저 크기 설정
options.add_experimental_option('detach', True)  # 브라우저 자동 닫힘 방지
driver = webdriver.Chrome(options=options)

# driver.get('http://localhost:8080')
driver.get(url)
driver.implicitly_wait(10)
driver.execute_script("document.body.style.zoom='100%'")
driver.find_element(By.ID, 'username').send_keys('ADMIN00000')
driver.find_element(By.ID, 'password').send_keys('qwer1234!')
driver.find_element(By.ID, 'password').send_keys(Keys.ENTER)
WebDriverWait(driver, 10).until(lambda d: d.current_url.endswith('/main'))
assert driver.current_url.endswith('/main')
driver.get(f'{url}/sym/usr/userList')
driver.execute_script('getAddForm()')

import uuid
user_uuid = str(uuid.uuid4())[:10].replace('-', '')
# 각 input에 값 입력
driver.find_element(By.ID, 'loginId').send_keys(user_uuid)
driver.find_element(By.ID, 'userNm').send_keys(user_uuid)

driver.find_element(By.ID, 'searchDept').click()
driver.implicitly_wait(3)
WebDriverWait(driver, 10).until(lambda d: d.find_element(By.CSS_SELECTOR, '.openDepartment').is_displayed())
driver.find_element(By.CSS_SELECTOR, '.openDepartment span[data-dept-id="3950000"]').click()
driver.find_element(By.CSS_SELECTOR, '.openDepartment span[data-dept-id="3950060"]').click()
WebDriverWait(driver, 10).until(lambda d: d.find_element(By.CSS_SELECTOR, '.openDepartment #sourceInnerContents tbody tr').is_displayed())
driver.find_element(By.CSS_SELECTOR, '.openDepartment #sourceInnerContents > table > tbody > tr > td:nth-child(1) > button').click()

import random
role_select = driver.find_element(By.CSS_SELECTOR, 'select[name="role"]')
_options = role_select.find_elements(By.TAG_NAME, 'option')
random_index = random.randint(0, len(_options) - 1)
_options[random_index].click()

driver.find_element(By.ID, 'userEml').send_keys('test@example.com')
driver.find_element(By.ID, 'userPswd').send_keys('qwer1234!')
driver.find_element(By.ID, 'userPswdCk').send_keys('qwer1234!')
driver.find_element(By.ID, 'mobileno').send_keys('01012345678')

# 약관동의 체크박스 클릭
button = driver.find_element(By.CSS_SELECTOR, '.btn-black.pop-custom-btn.waves-effect.waves-light').click()
button = driver.find_element(By.CSS_SELECTOR, '.btn.btnBlue').click()

# driver.quit()
# driver = webdriver.Chrome(options=options)
# driver.get(url)
# driver.implicitly_wait(10)
#
# driver.execute_script("document.body.style.zoom='100%'")
# driver.find_element(By.ID, 'username').send_keys(user_uuid)
# driver.find_element(By.ID, 'password').send_keys('qwer1234!')
# driver.find_element(By.ID, 'password').send_keys(Keys.ENTER)



