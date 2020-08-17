import time

from selenium import webdriver
from selenium.webdriver.common.keys  import Keys

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("明日之子")
driver.find_element_by_id("su").click()
driver.implicitly_wait(10)
#键盘组合键全选

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(5)
#剪切
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(5)
driver.find_element_by_id("kw").send_keys("明日之子4")
driver.find_element_by_id("su").click()
# driver.get("http://127.0.0.1:88/biz/user-login-L2Jpei8=.html")
# driver.maximize_window()
# driver.find_element_by_id("account").send_keys("admin")
# driver.find_element_by_id("account").send_keys(Keys.TAB )
# time.sleep(3)
# driver.find_element_by_name("password").send_keys("ymz17602921506")
# driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(6)
driver.quit()