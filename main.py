import requests
from bs4 import BeautifulSoup
import pandas as pd
from functions import parse

url = 'https://dominos.by'
r = requests.get(url)
soup = BeautifulSoup(r.text)
div = soup.find_all('div', {'class':'product-card'})
for item in div:
    res = parse(item)
    result = result.append(res, ignore_index=True)

result.to_excel('result.xlsx')