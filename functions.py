import pandas as pd

def parse(div):
    res = pd.DataFrame()

    name = ''

    ingridients = ''

    price = ''

    name=div.find('div', {'class': 'product-card__title'}).text

    ingridients=div.find('div', {'class':'product-card__description'}).text

    price=div.find('p', {'class':'product-card__modification-info-price'}).text

    res = res.append(pd.DataFrame([[name, ingridients, price]], columns = ['Name', 'Ingridients', 'Price']))
    return(res)

