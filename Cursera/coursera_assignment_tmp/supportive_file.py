from django.http import HttpResponse
import requests

params = {
    'a': '4',
    'b': '3'
}


def simple_route():
    request = requests.post('http://127.0.0.1:8000/routing/sum_get_method/?a=1&b=2')
    print(request.status_code)


if __name__ == '__main__':
    simple_route()