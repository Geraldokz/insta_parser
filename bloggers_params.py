import csv
import json
import os
import subprocess
import time

command = """curl '{url}' \
  -H 'authority: www.instagram.com' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"' \
  -H 'accept: */*' \
  -H 'x-ig-www-claim: hmac.AR38rMisrmYaz40kekhzhKC9pmdyRN5qXV_v_ShdO3YAKvLP' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36' \
  -H 'x-ig-app-id: 936619743392459' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.instagram.com/maeo_savina/?hl=ru' \
  -H 'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'cookie: mid=YJ9lHwAEAAHPXCIjjogUIbXPo_fF; ig_did=02015BD5-98E7-4368-9BEF-DED08609E5A0; ig_nrcb=1; csrftoken=bocjqxmqV7pFfxwqnOR3QJUOBlmAT01m; ds_user_id=34680082206; sessionid=34680082206%3AiWh6wyYYcDLxMQ%3A2; shbid=2232; shbts=1621659159.080917; rur=FTW' \
  --compressed > json/tmp.json"""

bloggers_params_list = []


def _get_url(username):
    return f'https://www.instagram.com/{username}/?__a=1'


def get_bloggers_params_list(username_list):
    bloggers_quantity = len(username_list)
    index = 1
    print(f'Кол-во блоггеров {bloggers_quantity}\n')

    for user in username_list:
        result = subprocess.run(command.format(url=_get_url(user[0])), shell=True, capture_output=True)
        if result.returncode != 0:
            print(f'Ошибка при получении параметров блоггера {user[0]}')
            break
        else:
            print(f'Обработано {index}/{bloggers_quantity}')

        with open('json/tmp.json', 'r') as f:
            data = json.load(f)

        username = data['graphql']['user']['username']
        subscribers = data['graphql']['user']['edge_followed_by']['count']
        subscribe_to = data['graphql']['user']['edge_follow']['count']
        tag = user[1]

        bloggers_params_list.append([username, subscribers, subscribe_to, tag])

        index += 1
        time.sleep(1)

    os.remove('json/tmp.json')
    return bloggers_params_list


def write_bloggers_to_table(bloggers_list):
    with open('bloggers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Username', 'Подписчиков', 'Подписан на', 'Тэг'])
        for blogger in bloggers_list:
            username = blogger[0]
            subscribers = blogger[1]
            subscribe_to = blogger[2]
            tag = blogger[3]
            writer.writerow([username, subscribers, subscribe_to, tag])
