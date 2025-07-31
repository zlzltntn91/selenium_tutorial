import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = "https://hsc1170.synology.me/sdsms_new/html/list-10-02-01.html#"
options = Options()

options.add_argument("--window-position=200,400")
options.add_argument("--window-size=1200,1200")  # 브라우저 크기 설정

options.add_experimental_option('detach', True)  # 브라우저 자동 닫힘 방지

driver = webdriver.Chrome(options=options)


def get_icon_path():
    driver.get(url)
    driver.implicitly_wait(10)
    driver.execute_script("document.body.style.zoom='50%'")
    driver.find_element(By.ID, 'openFavorites').click()

    div = driver.find_element(By.CLASS_NAME, 'popup-layer')
    for icon in div.find_elements(By.TAG_NAME, 'li'):
        icon_name = icon.find_element(By.TAG_NAME, 'i').get_attribute('class')
        menu_name = icon.find_element(By.TAG_NAME, 'span')
        print(f"update comtnmenuinfo set relate_image_nm = '{icon_name}' where menu_nm = '{menu_name.text}' and upper_menu_no != 0;")

get_icon_path()
