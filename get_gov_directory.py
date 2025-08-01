import openpyxl
import xlrd
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options

codes = []
def get_excel():
    wb = xlrd.open_workbook('행정표준코드 조회자료 2.xls')
    sheet = wb.sheet_by_index(0)
    rows = (sheet.row(i) for i in range(sheet.nrows))
    for row_num, row in enumerate(rows):
        if row_num == 798:
            break
        code = row[2].value
        name = row[3].value
        codes.append({"code": code, "name": name})

get_excel()

url = "https://www.dir.go.kr/dsm/ui/index.do"
options = Options()

options.add_argument("--window-position=200,400")
options.add_argument("--window-size=1200,1200")  # 브라우저 크기 설정

options.add_experimental_option('detach', True)  # 브라우저 자동 닫힘 방지
driver = webdriver.Chrome(options=options)

selenium.webdriver.Chrome()





