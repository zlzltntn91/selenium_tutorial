import openpyxl
import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

codes = []


def get_excel():
    wb = openpyxl.load_workbook('기관코드 조회자료_t.xlsx')
    sheet = wb.active
    for row_num, row in enumerate(sheet.iter_rows(values_only=True, min_row=2)):
        if row_num == 798:
            break
        code = row[0]
        name = row[1]
        print(code)
        print(name)
        codes.append({"code": code, "name": name})


get_excel()

url = "https://www.dir.go.kr/dsm/ui/index.do"
options = Options()

options.add_argument("--window-position=200,400")
options.add_argument("--window-size=1200,1200")  # 브라우저 크기 설정
options.add_experimental_option('detach', True)  # 브라우저 자동 닫힘 방지
driver = webdriver.Chrome(options=options)
driver.get(url)

req_url = "https://www.dir.go.kr/dsm/dirmanage/OrgSearch.do"

for code in codes:

    ous = code["name"].split(" ")[::-1]
    query_string = ""
    for ou in ous:
        query_string += f"ou={ou},"
    query_string += "o=government of korea,c=kr"
    script = driver.execute_script(f"""
        return fetch('{req_url}?dn={query_string}', {{
            method: 'POST',
            headers: {{
                'Content-Type': 'application/x-www-form-urlencoded'
            }}
        }})
        .then(response => response.text())
        .then(text => text)
    """)
    soup = BeautifulSoup(script, "html.parser")
    table = soup.find("tbody")
    print(table)


time.sleep(1)
print(script)
print('end')
driver.quit()

