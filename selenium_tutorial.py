# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:03:03 2020

@author: Joyce Wang
Title: Selenium Tutorial
"""

# Refer to the offical website at:
# https://selenium-python.readthedocs.io/index.html
# If need to install selenium, use "pip install selenium"

# STEP 0 - Initialization
import os
from selenium import webdriver
os.chdir(r'C:\Users\admin\Box\CODING\Github\Summer-Research-2020')
print(os.getcwd())

# STEP 1 - Prepare the driver 
# Depending on the browser used, download the appropriate driver at the website, I am using Chrome:
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# Then put the driver in the current working folder

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')

