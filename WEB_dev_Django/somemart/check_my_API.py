import requests

item = {
    "title": "item_1",
    "description": "",
    "price": 20
}

rewiews = {
    "text": "Best. Cheese. Ever.",
    "grade": 9
}


def check_item():
    response = requests.post("http://127.0.0.1:8000/api/v1/goods/", json=item, auth=('user', 'password'))
    print(response.content)


def check_rewiews():
    item_id = 2  # !id item`а в бд!
    response = requests.post(f"http://127.0.0.1:8000/api/v1/goods/{item_id}/reviews/", json=rewiews)
    print(response.content)


def check_viewinfo():
    item_id = 10
    response = requests.get(f"http://127.0.0.1:8000/api/v1/goods/{item_id}/")
    print(response.content)

if __name__ == '__main__':
    check_item()
    # check_rewiews()
    # check_viewinfo()