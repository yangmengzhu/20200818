import time

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.minimize_window()
# driver.find_element_by_id("kw").send_keys("毛不易")
# driver.find_element_by_id("su").submit()
# time.sleep(6)
# # title=driver.title
# # print("title="+title)
#
# url=driver.current_url
# print("url="+url)

time.sleep(6)
driver.quit()