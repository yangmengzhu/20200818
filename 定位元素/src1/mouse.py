import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("薛之谦")
su1=driver.find_element_by_id("su")
#鼠标右击
ActionChains(driver).context_click(su1).perform()
time.sleep(3)
#双击鼠标
ActionChains(driver).double_click(su1).perform()
time.sleep(3)
#拖动鼠标
title=driver.find_element_by_id("su")
target=driver.find_element_by_link_text("薛之谦_百度百科")
ActionChains(driver).drag_and_drop(title,target).perform()
#移动
ActionChains(driver).move_to_element(target).perform()
driver.quit()