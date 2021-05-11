import pandas as pd


def parse_table(table):
    res = pd.DataFrame()

    name = ''

    user = ''

    cena = ''

    name_tr = table.find('div',{'class': 'product-card__title'})
    # получаю текст вопроса
    name = name_tr.find('div').text.strip()

    ingridients_tr = name_tr.find('div', {'class': 'product-card__description'})
    ingridients = ingridients_tr.text.strip()

    # ответы
    cena_tr = table.find('p', {'class': 'product-card__modification-info-price'})
    cena = cena_tr.find_all('#text')[0].find('div').text.strip()

    res = res.append(pd.DataFrame([
        [name, ingridients, cena]
    ], columns=['Name', 'Ingridients', 'Cena_na_angliyskom']), ignore_index=True)
    return res