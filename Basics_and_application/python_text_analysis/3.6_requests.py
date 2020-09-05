import requests
import sys
from operator import itemgetter

sys.stdin = open("for_3.6.txt")

params = {
            'json': 'true'
}


def good_number():
    for num in sys.stdin:
        num = int(num.strip())
        api_url = f"http://numbersapi.com/{num}/math"
        res = requests.get(api_url, params=params)
        data = res.json()

        if data['found']:
            print('Interesting')
        else:
            print('Boring')


# good_number()

def task_2():
    import json


    client_id = 'a3c85a96a2f1afa01d7e'
    client_secret = 'dfea47f82e68ea5c8fec65ddf0ea7323'

    r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                      data={
                          "client_id": client_id,
                          "client_secret": client_secret
                      })

    j = json.loads(r.text)

    token = j["token"]

    headers = {"X-Xapp-Token": token}

    artists = {}

    with open("for_3.6(2).txt", encoding='utf-8') as file:
        for line in file:
            r = requests.get(f"https://api.artsy.net/api/artists/{line.strip()}", headers=headers)
            j = json.loads(r.text)
            artists.update({j['sortable_name']: int(j['birthday'])})
        res = sorted(artists.items(), key=itemgetter(1, 0))


    with open("res_3.6(2).txt", 'w', encoding='utf-8') as file:
        for artist in res:
            file.write(str(artist[0]) + '\n')

task_2()