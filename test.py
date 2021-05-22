import csv
import subprocess
import json

command = """curl 'https://www.instagram.com/web/search/topsearch/?context=blended&query=%D0%A2%D1%80%D0%B5%D0%BD%D0%B5%D1%80&rank_token=0.457716893351779&include_reel=true' \
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
  -H 'referer: https://www.instagram.com/drakeofficlal/?hl=ru' \
  -H 'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'cookie: mid=YJ9lHwAEAAHPXCIjjogUIbXPo_fF; ig_did=02015BD5-98E7-4368-9BEF-DED08609E5A0; ig_nrcb=1; csrftoken=bocjqxmqV7pFfxwqnOR3QJUOBlmAT01m; ds_user_id=34680082206; sessionid=34680082206%3AiWh6wyYYcDLxMQ%3A2; shbid=2232; shbts=1621659159.080917; rur=FTW' \
  --compressed > json/followers.json"""

command_2 = """curl 'https://www.instagram.com/afanaseva.trener/?__a=1' \
  -H 'authority: www.instagram.com' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"' \
  -H 'accept: */*' \
  -H 'x-ig-www-claim: hmac.AR38rMisrmYaz40kekhzhKC9pmdyRN5qXV_v_ShdO3YAKn-7' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36' \
  -H 'x-ig-app-id: 936619743392459' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.instagram.com/gimme_asecond/' \
  -H 'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'cookie: mid=YJ9lHwAEAAHPXCIjjogUIbXPo_fF; ig_did=02015BD5-98E7-4368-9BEF-DED08609E5A0; ig_nrcb=1; csrftoken=bocjqxmqV7pFfxwqnOR3QJUOBlmAT01m; ds_user_id=34680082206; sessionid=34680082206%3AiWh6wyYYcDLxMQ%3A2; shbid=2232; shbts=1621659159.080917; rur=FTW' \
  --compressed > user.json"""

# result = subprocess.run(command_2, shell=True, capture_output=True)
# print(result)

with open('user.json', 'r') as f:
    data = json.load(f)

    biography = data['graphql']['user']['biography']
    username = data['graphql']['user']['username']
    full_name = data['graphql']['user']['full_name']
    subscribers = data['graphql']['user']['edge_followed_by']['count']
    subscribe_to = data['graphql']['user']['edge_follow']['count']

    print(username)
    print(full_name)
    print(biography)
    print(f'Подписчиков: {subscribers}')
    print(f'Подписан на: {subscribe_to}')

with open('bloggers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Username', 'Полное имя', 'Подписчиков', 'Подписан на'])
    writer.writerow([username, full_name, subscribers, subscribe_to])
