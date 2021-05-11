import pandas as pd


def parse_table(card):
    res = pd.DataFrame()

    name = ''

    ingridients = ''

    cena = ''


    # получаю текст вопроса
    name = card.find('div').text.strip()

    ingridients_tr = card.find('div', {'class': 'product-card__description'})
    ingridients = ingridients_tr.text.strip()

    # ответы
    cena_tr = card.find('p', {'class': 'product-card__modification-info-price'})
    cena = cena_tr.find_all('#text')[0].find('div').text.strip()

    res = res.append(pd.DataFrame([
        [name, ingridients, cena]
    ], columns=['Name', 'Ingridients', 'Cena_na_angliyskom']), ignore_index=True)
    return res