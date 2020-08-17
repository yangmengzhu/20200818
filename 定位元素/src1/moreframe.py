import os
import time

from selenium import webdriver
driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('D:/360安全浏览器下载/selenium2html/frame.html')
driver.get(file_path)
driver.maximize_window()
time.sleep(6)
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("毛不易")
driver.find_element_by_id("su").submit()
time.sleep(6)
#跳转到默认页面
driver.switch_to.default_content()
driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()
time.sleep(5)
driver.quit()