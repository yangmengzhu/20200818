import time

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("毛不易")
driver.find_element_by_id("su").submit()
#浏览器最大化
driver.maximize_window()
time.sleep(6)
driver.minimize_window()
time.sleep(6)
driver.set_window_size(400,800)
time.sleep(6)
driver.maximize_window()

#浏览器的前进和后退
driver.back()
time.sleep(6)
driver.forward()
time.sleep(6)
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(6)
js1="var q=document.documentElement.scrollTop=0"
time.sleep(6)
#同时控制滚动条
driver.quit()

