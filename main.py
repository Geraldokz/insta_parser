import sys

from bloggers_list import get_all_bloggers_json, get_bloggers_username_list
from bloggers_params import get_bloggers_params_list, write_bloggers_to_table

city = sys.argv[1]

with open(f'{sys.argv[2]}', 'r') as f:
    tags = f.read()
    tags_list = tags.split(',')

# Получаем всех блогеров по тематикам в json формате
get_all_bloggers_json(tags_list, city)

# Получаем список username всех блогеров
username_list = get_bloggers_username_list()

# Получаем список блогеров с username, кол-во подписчиков и подписок
bloggers_list = get_bloggers_params_list(username_list)

# Записываем данные в таблицу
write_bloggers_to_table(bloggers_list)

print('\nУраааа, все готово!!!')

