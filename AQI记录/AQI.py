from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import urllib
import html5lib

aqivalue = []
filename = str(datetime.date.today())
i=0
while True:
    while (time.localtime().tm_min==0):
        hour = str(time.localtime().tm_hour)
        driver = webdriver.Chrome()
        driver.get("http://aqicn.org/city/nanjing/cn/")
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "citydivmain"))
            )
            soup = BeautifulSoup(driver.page_source, 'html5lib')
        finally:
            driver.quit()
    ##headers={"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    ##req = urllib.request.Request("http://aqicn.org/city/nanjing/cn/", headers=headers)
    ##url=urllib.request.urlopen(req)
    ##soup=BeautifulSoup(url,"html5lib")
        td = soup.find('div', {"id": "citydivmain"})
        div = soup.find('div', {'class': 'aqivalue'})
        aqi = div.text
        aqivalue.append(aqi)
        file = open("AQI/AQI"+filename+".txt", "a+")
        file.write(hour+","+aqi+"\n")
        file.close()
        time.sleep(60)

