from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import html5lib
import re
import datetime
from urllib.request import urlretrieve

name = str(datetime.date.today())
driver = webdriver.Chrome()
driver.get("https://www.cn.bing.com")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bgDiv"))
    )
    soup = BeautifulSoup(driver.page_source, 'html5lib')
finally:
    driver.quit()
div = soup.find('div', {'id': 'bgDiv'})
style = div['style']
Link = re.findall("https.*.jpg",style)
print(Link[0])
urlretrieve(Link[0], "Bing/"+name+".jpg")
