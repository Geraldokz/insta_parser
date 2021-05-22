import glob
import json
import os
import subprocess
import time
import urllib.parse

url_base = 'https://www.instagram.com/web/search/topsearch/?'

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
  -H 'referer: https://www.instagram.com/afanaseva.trener/?hl=ru' \
  -H 'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'cookie: mid=YJ9lHwAEAAHPXCIjjogUIbXPo_fF; ig_did=02015BD5-98E7-4368-9BEF-DED08609E5A0; ig_nrcb=1; csrftoken=bocjqxmqV7pFfxwqnOR3QJUOBlmAT01m; ds_user_id=34680082206; sessionid=34680082206%3AiWh6wyYYcDLxMQ%3A2; shbid=2232; shbts=1621659159.080917; rur=FTW' \
  --compressed > json/{tag}.json """

tags_list = ['Тренер', 'Блогер', 'Психолог']


def _get_url(tag, city):
    url_params = {
        'context': 'blended',
        'query': f'{tag}_{city}',
        'rank_token': '0.27781472827297815',
        'include_reel': '0.27781472827297815'
    }
    return url_base + urllib.parse.urlencode(url_params)


def get_all_bloggers_json(tags, city):
    for tag in tags:
        print(f'Получаем json {tag}')
        url = _get_url(tag, city)
        result = subprocess.run(command.format(url=url, tag=tag), shell=True, capture_output=True)
        if result.returncode != 0:
            f'Ошибка при получении json {tag} {city}'
        else:
            print(f'json {tag} {city} получен\n')
        time.sleep(3)


def get_bloggers_username_list():
    files = glob.glob('json/*.json')
    username_list = []

    for file in files:
        tag, ext = os.path.splitext(os.path.basename(file))
        with open(file, 'r') as f:
            data = json.load(f)

        for user in data['users']:
            username_list.append([user['user']['username'], tag])

    return username_list


if __name__ == '__main__':
    # get_all_bloggers_json(tags_list, 'Новосибирск')
    # print(get_bloggers_username_list())
    bloggers = get_bloggers_username_list()

    for blogger in bloggers:
        print(blogger[0])
