import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=os.path.curdir+"/geckodriver")

driver.get("http://igor:password@localhost:80")
assert "SoftDes" in driver.title

driver.find_element_by_id("resposta").send_keys(os.getcwd()+"/desafio.py")
btn = driver.find_element_by_class_name("btn-primary")
btn.click() 
time.sleep(0.3)
table = driver.find_element_by_class_name("table")
rows = table.find_elements_by_tag_name("tr")
cols = rows[1].find_elements_by_tag_name("td")
assert "Erro" in cols[2].text 

time.sleep(0.2)
driver.find_element_by_id("resposta").send_keys(os.getcwd()+"/desafio_certo.py")
btn = driver.find_element_by_class_name("btn-primary")
btn.click() 
time.sleep(0.3)
table = driver.find_element_by_class_name("table")
rows = table.find_elements_by_tag_name("tr")
cols = rows[1].find_elements_by_tag_name("td")
assert "OK!" in cols[2].text 



time.sleep(5)
driver.close()