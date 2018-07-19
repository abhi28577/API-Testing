#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:18:17 2018

@author: abhi28577
"""

# Getting Current URL

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Safari()
driver.get('http://www.nennepedia.org')
driver.maximize_window()

elem=driver.find_element_by_link_text('Heart Stroke')
elem.click()

print('Clicked Hyperlink Text has a URL: ' + driver.current_url)

time.sleep(5)

driver.close()

