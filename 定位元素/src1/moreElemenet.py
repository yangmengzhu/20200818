# from selenium import webdriver
# import time
# import os
# driver = webdriver.Firefox()
# file_path = 'file:///' + os.path.abspath('D:/xampp/checkbox.html')
# driver.get(file_path)
# # 选择页面上所有的input，然后从中过滤出所有的checkbox 并勾选之
# inputs = driver.find_elements_by_tag_name('input')
# for input in inputs:
#  if input.get_attribute('type') == 'checkbox':
#     input.click()
# time.sleep(2)
# driver.quit()
import os
import time

from selenium import webdriver
driver=webdriver.Firefox()
driver.maximize_window()
file_path='file:///'+os.path.abspath('D:/xampp/checkbox.html')
inputs=driver.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type')=='checkbox':
        input.click()
time.sleep(6)
driver.quit()


