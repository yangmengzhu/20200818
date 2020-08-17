import os
import time

from selenium import webdriver
driver=webdriver.Firefox()
#file_path='file:///'+os.path.abspath('D:/360安全浏览器下载/selenium2html/drop_down.html')

# inputs=driver.find_elements_by_tag_name('option')
# # for input in inputs:
# #       if input.get_attribute('value')== '9.03':
# #           input.click()
# inputs[3].click()
# driver.find_element_by_xpath("//*[@id='ShippingMethod']/option[3]").click()
file_path='file:///'+os.path.abspath('D:/360安全浏览器下载/selenium2html/alert.html')
driver.get(file_path)
driver.maximize_window()
driver.find_element_by_id("tooltip").click()
time.sleep(5)
alert=driver.switch_to.alert
alert.accept()

time.sleep(5)
driver.quit()