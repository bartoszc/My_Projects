"""Fetch Current Weather - Get the current weather for a given zip/postal code.
Optional: Try locating the user automatically.  """

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


URL = 'https://mylocation.org/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
location = soup.find("td", text="City").find_next_sibling("td").text

browser = webdriver.Chrome()
browser.get('https://google.com/')
searchElem = browser.find_element(By.NAME, 'q')
query = 'pogoda ' + location
searchElem.send_keys(query)
searchElem.send_keys(Keys.ENTER)
