import os
import time

import urllib.request
from selenium import webdriver
browser=webdriver.Chrome('chromedriver.exe')
browser.get('url to visit')
url = "url from where the image will be downloaded"

r = urllib.request.urlopen(url)
with open("image.jpg", "wb") as f:
    f.write(r.read())
imgname = os.path.abspath("image.jpg")
time.sleep(2)
browser.get("https://web.whatsapp.com/")
time.sleep(19)

browser.find_element_by_xpath('//span[@title="Group name"]').click()
time.sleep(1.5)

browser.find_element_by_xpath('//div[@title="Attach"]').click()
time.sleep(2)

browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(imgname)
time.sleep(2)

browser.find_element_by_xpath('//span[@data-icon="send"]').click()








