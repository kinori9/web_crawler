import time
from urllib.request import urlopen
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

connect_site = ""
driver = webdriver.Chrome()
driver.get(connect_site)
i = 0
link = []
for i in range(0,100):
    time.sleep(3)
    driver.find_element_by_css_selector(".sprites-navigator-right").click()
    try:
        img = driver.find_element_by_xpath('//img')
        
    except:
        img = driver.find_element_by_xpath('//img')

    a = img.get_attribute('src')    
    urllib.request.urlretrieve(a,'./img/'+str(i)+'.jpg')
        

    
