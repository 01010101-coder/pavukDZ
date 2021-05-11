import pandas as pd


def parse(div):
    res = pd.DataFrame()

    name = ''

    ingridients = ''

    price = ''

    name = div.find('div', {'class': 'product-card__title'}).text.strip()

    ingridients = div.find('div', {'class': 'product-card__description'}).text.strip()

    price = div.find('p', {'class': 'product-card__modification-info-price'}).text.strip()

    res = res.append(pd.DataFrame([[name, ingridients, price]], columns=['Name', 'Ingridients', 'Price']))
    return res  # скобки не нужны
