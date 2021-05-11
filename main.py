import requests
from bs4 import BeautifulSoup
from functions import parse_table
import pandas as pd


url = f'https://www.dominos.by/'
r = requests.get(url)  # подключаюсь по указанному урлу
result = pd.DataFrame()  # создаю таблицу
soup = BeautifulSoup(r.text, features='html.parser')  # это сам парсер
tables = soup.find_all('div ', {'class': 'product-card'})


for item in tables:
    res = parse_table(item)  # я вызываю функцию парсинга для каждой таблицы с сайта
    result = result.append(res, ignore_index=True)

result.to_excel('result.xlsx')

# .find('table') - ищет первое вхождение элемента в тексте
# .find_all('table') - ищет ВСЕ вхождения элемента в тексте
# find('table').text - возврат текста, который находится в объекте
# find('table').get('href') - вернет ссылки


#with open('test.html', 'w') as f:
    # открываю файл test.html в режиме записи (write)
#    f.write(r.text)  # И записываю в него ответ от сайта