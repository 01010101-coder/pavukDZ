import requests
from bs4 import BeautifulSoup
import pandas as pd
from functions import parse

result = pd.DataFrame()

url = 'https://dominos.by'
r = requests.get(url)
soup = BeautifulSoup(r.text, features='html.parser')
div = soup.find_all('div', {'class': 'product-card'})
for item in div:
    res = parse(item)
    result = result.append(res, ignore_index=True)

result.to_excel('result.xlsx')