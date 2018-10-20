#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selene.driver import SeleneDriver
from webdriver_manager.chrome import ChromeDriverManager

# run chrome headless
options = Options()
options.add_argument('--headless')

# install chromedriver if not found and start chrome
driver = SeleneDriver.wrap(webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options))

# search 'python' in google
driver.get('https://www.google.co.jp/')
input = driver.find_element_by_name('q')
input.send_keys('Python')
input.send_keys(Keys.RETURN)

# save screen shot
driver.save_screenshot('result.png')

driver.quit()

