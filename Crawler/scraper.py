from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()

driver.get('https://www.youtube.com/watch?v=RGB-wlatStc')

driver.execute_script('window.scrollTo(1, 500);')
time.sleep(5)

comment_obj = driver.find_element_by_id('comment')

print(comment_obj.text)

driver.quit()
