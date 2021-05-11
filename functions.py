import pandas as pd

def parse(cards):
    res = pd.DataFrame()

    name = ''

    ingridients = ''

    price = ''

    name=cards.find('div', {'class': 'product-card__title'}).text

    ingridients=cards.find('div', {'class':'product-card__description'}).text

    price=cards.find('div', {'class':'product-card__modification-info-price'}).text

    res = res.append(pd.DataFrame([[name, ingridients, price]], columns = ['Name', 'Ingridients', 'Price']))
    return(res)

