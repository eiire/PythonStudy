from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    params = {
        'date_req': date
    }


    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp", params=params)  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'lxml')
    values = {}

    for val in soup('valute'):
        values.update({str(val.find('charcode').string):
                           [Decimal(val.find('value').string.replace(',', '.')),
                            Decimal(val.find('nominal').string.replace(',', '.'))]})

    # for e, v in values.items():
    #     print(e, v)

    if cur_from == 'RUR':
        rate = values[cur_to][1] / values[cur_to][0]
        res = amount * rate
    elif cur_to == 'RUR':
        rate = values[cur_from][0] / values[cur_from][1]
        res = amount * rate
    else:
        rate_from = values[cur_from][0] / values[cur_from][1]
        res_rub = rate_from * amount

        rate_to = values[cur_to][0] / values[cur_to][1]
        res = res_rub / rate_to

    return res.quantize(Decimal("1.0000"))
