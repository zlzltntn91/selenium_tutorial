import time
from time import sleep

from selenium_helper import SeleniumHelper
from selenium.webdriver.common.by import By

url = "http://localhost:8080"
helper = SeleniumHelper(url)
helper.login()

helper.get('/chk/imp/BSC0000000000000191/CPLUp6dtA56NIRLsWqK2WSVXS1euunfi/PRDUp2UNpuFBeAhcLJPzKyxq1p7qvvut')
