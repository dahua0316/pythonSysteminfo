
from selenium import webdriver
import time


driver = webdriver.Chrome()     # 创建Chrome对象.
# 操作这个对象.
driver.get('https://www.baidu.com')     # get方式访问百度.
time.sleep(2)
driver.quit()
