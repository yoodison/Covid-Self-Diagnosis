# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import time
 
area = '10'
school_level = '4'
school_name = 'XXXX고등학교'
name = 'OOO'
birth = '010123'
password = '0123'
 
driver = webdriver.Firefox()
driver.get('https://hcs.eduro.go.kr')
driver.find_elements_by_id('btnConfirm2')[0].click()
time.sleep(1)
driver.find_elements_by_class_name('searchBtn')[0].click()
time.sleep(1)
 
select = Select(driver.find_elements_by_tag_name('select')[0])
select.select_by_value(area)
select = Select(driver.find_elements_by_tag_name('select')[1])
select.select_by_value(school_level)
 
login = driver.find_element_by_class_name("searchArea");
login.send_keys(school_name)
 
time.sleep(1)
driver.find_elements_by_tag_name('td')[3].click()
time.sleep(1)
driver.find_element_by_partial_link_text(school_name).click()
time.sleep(1)
driver.find_elements_by_class_name('layerFullBtn')[0].click()
time.sleep(1)
 
login = driver.find_elements_by_class_name("input_text_common")[1]
login.send_keys(name)
login = driver.find_elements_by_class_name("input_text_common")[2]
login.send_keys(birth)
 
element = driver.find_element_by_id('btnConfirm')
driver.execute_script("arguments[0].click();", element)
time.sleep(1)
 
driver.find_element_by_class_name('input_text_common').click()
time.sleep(0.5)
driver.find_element_by_css_selector(f'div[aria-label=\'{password[0]}\']').click()
time.sleep(0.5)
driver.find_element_by_css_selector(f'div[aria-label=\'{password[1]}\']').click()
time.sleep(0.5)
driver.find_element_by_css_selector(f'div[aria-label=\'{password[2]}\']').click()
time.sleep(0.5)
driver.find_element_by_css_selector(f'div[aria-label=\'{password[3]}\']').click()
time.sleep(0.5)
 
time.sleep(1)
driver.find_element_by_id('btnConfirm').click()
time.sleep(1)
 
driver.find_elements_by_class_name('btn')[0].click()
time.sleep(1)
driver.find_elements_by_tag_name('label')[0].click()
driver.find_elements_by_tag_name('label')[2].click()
driver.find_elements_by_tag_name('label')[4].click()
driver.find_elements_by_id('btnConfirm')[0].click()
time.sleep(1)
driver.quit()
