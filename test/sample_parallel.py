#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selene.driver import SeleneDriver
from webdriver_manager.chrome import ChromeDriverManager
from joblib import Parallel, delayed

# search 'keyword' in google
def google(url, keyword):
    # run chrome headless
    options = Options()
    options.add_argument('--headless')
    driver = SeleneDriver.wrap(webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options))
    driver.get(url)
    input = driver.find_element_by_name('q')
    input.send_keys(keyword)
    input.send_keys(Keys.RETURN)

    # save screen shot
    driver.save_screenshot(keyword + '.png')

    driver.quit()

url = 'https://www.google.co.jp/'
keywords = ['Python', 'Google', 'Selenium']

# n_jobs=-1 means use all of the resources you can`
Parallel(n_jobs=-1)(delayed(google)(url,keyword) for keyword in keywords)
