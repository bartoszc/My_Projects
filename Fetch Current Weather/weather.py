"""Fetch Current Weather - Get the current weather for a given zip/postal code.
Optional: Try locating the user automatically.  """

import requests
from bs4 import BeautifulSoup

URL = 'https://mylocation.org/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
a = soup.find("td", text="City").find_next_sibling("td").text
print(a)

#
# ee