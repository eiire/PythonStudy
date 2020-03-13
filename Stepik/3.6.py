import requests
import sys

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


good_number()