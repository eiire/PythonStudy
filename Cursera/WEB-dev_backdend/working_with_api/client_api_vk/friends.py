import requests
import datetime
from operator import itemgetter

access_token = '32514f9b32514f9b32514f9b023221181b3325132514f9b6c21acb209c0309a4cd59dbb'
version = '5.71'
fields = 'bdate'

user_params = {
            "v": version,
            "access_token": access_token,
            "user_ids": ""
}

friends_params = {
            "v": version,
            "access_token": access_token,
            "user_id": "",  # 210700286|LindseyStirling
            "fields": fields
}

date_now = datetime.datetime.now()


def calc_age(uid):
    """ Подсчет распределения возрастов друзей для указанного пользователя. """
    numb_age = 1
    counter_age = {}

    if type(uid) == str:
        user_params["user_ids"] = uid
        url_id_user = 'https://api.vk.com/method/users.get'
        response_1 = requests.get(url_id_user, params=user_params)
        friends_params["user_id"] = response_1.json()["response"][0]["id"] # text-->json-->

    elif type(uid) == int:
        user_params["user_ids"] = uid
        url_id_user = 'https://api.vk.com/method/users.get'
        response_1 = requests.get(url_id_user, params=user_params)
        friends_params["user_id"] = response_1.json()["response"][0]["id"]
    else:
        return -1

    url_list_friend = 'https://api.vk.com/method/friends.get'
    response_2 = requests.get(url_list_friend, params=friends_params)
    for user in response_2.json()["response"]["items"]:
        try:
            age_user = date_now.year - int(user["bdate"].split('.')[2])
            try:
                counter_age[age_user] = counter_age[age_user] + 1
            except:
                counter_age.update({age_user: numb_age})
        except:
            # print("IncorrectBirthday")
            pass

    print(counter_age)
    s = sorted(counter_age.items(), key=itemgetter(0))
    y = sorted(s, key=itemgetter(1), reverse=True)

    return y


if __name__ == '__main__':
    res = calc_age(106275424)
    print(res)
