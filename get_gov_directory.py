import openpyxl
import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

codes = []
results = {}


def get_excel():
    wb = openpyxl.load_workbook('기관코드 조회자료 2.xlsx')
    sheet = wb.active
    for row_num, row in enumerate(sheet.iter_rows(values_only=True, min_row=2)):
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

driver.find_element(by="css selector", value=".btn_normal.fnc_submit1.ui-button.ui-corner-all.ui-widget").click()

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
    tbody = soup.find("tbody")
    trs = tbody.find_all("tr")

    data = []
    for tr in trs:
        v = tr.find("td").get_text(strip=True)
        data.append(v)

    dic = {}
    if (len(data) < 7):
        print("데이터가 충분하지 않습니다:", data)
        continue

    dic["name"] = data[0]
    dic["code"] = data[1]
    dic["top_code"] = data[2]
    dic["up_code"] = data[3]
    dic["full_name"] = data[4]
    dic["degree"] = data[5]
    dic["sn"] = data[6]
    results[dic["code"]] = dic

    time.sleep(0.5)

i = 1
# print("insert into comtn_dept_info (dept_id, up_dept_id, dept_nm, dept_lv, dept_sn, hghrk_dept_id, rprs_dept_id, scrn_dept_nm, whol_dept_nm, inst_lv, abl_yn, crt_dt, rgtr_id, reg_dt) values ('6410000', null, '경기도', 1, 1, '6410000', '0000000', '경기도', '경기도', 1, 'Y', '20250803000000', 'SYSTEM', '20250803000000');")
# print("insert into comtn_dept_info (dept_id, up_dept_id, dept_nm, dept_lv, dept_sn, hghrk_dept_id, rprs_dept_id, scrn_dept_nm, whol_dept_nm, inst_lv, abl_yn, crt_dt, rgtr_id, reg_dt) values ('6410000', null, '경기도', 1, 1, '6410000', '0000000', '경기도', '경기도', 1, 'Y', '20250803000000', 'SYSTEM', '20250803000000');")
for code, result in results.items():
    print(
        f"insert into comtn_dept_info (dept_id, up_dept_id, dept_nm, dept_lv, dept_sn, hghrk_dept_id, rprs_dept_id, scrn_dept_nm, whol_dept_nm, inst_lv, abl_yn, crt_dt, rgtr_id, reg_dt) values ('{result['code']}', '{result['up_code']}', '{result['name']}', {result['degree']}, {i}, '{result['top_code']}', '{result['up_code']}', '{result['name']}', '{result['full_name']}', {result['degree']}, 'Y', '20250803000000', 'SYSTEM', '20250803000000');"
    )
    i += 1
driver.quit()
