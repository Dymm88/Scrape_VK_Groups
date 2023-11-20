import os
import vk_api
import vk_api.exceptions
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from progress.bar import IncrementalBar


load_dotenv(find_dotenv())
TOKEN = os.environ.get("TOKEN")
session = vk_api.VkApi(token=TOKEN)


def get_groups_list(user_id: int) -> list[int]:
    friends = session.method('friends.get', {'user_id': user_id})
    groups_list = []
    bar = IncrementalBar('Countdown', max=friends['count'])
    for friend in friends['items']:
        try:
            group = session.method('groups.get', {'user_id': friend})
            groups_list.extend(group['items'])
            bar.next()
        except vk_api.exceptions.ApiError:
            bar.next()
            continue
    bar.finish()
    return groups_list


def sort_groups(groups_list: list[int]) -> list[int]:
    df = pd.Series(groups_list)
    sort_df = df.value_counts(sort=True)
    sort_list = list(sort_df.index)
    return sort_list


def output_top_groups(sort_list: list[int], quantity: int) -> list[str]:
    top_list = []
    count = 0
    for group in sort_list:
        group_id = session.method('groups.getById', {'group_id': group})
        group_name = group_id[0]
        count += 1
        top_list.append(group_name['name'])
        print(f"{count}. {group_name['name']}")
        if count == quantity:
            break
    return top_list


def write_file(top_list: list[str], user_id: int):
    user = session.method('users.get', {'user_ids': user_id})
    with open(f"../results/{user[0]['first_name']} {user[0]['last_name']}.txt", 'w', encoding='utf8') as file:
        for element in top_list:
            file.write(element + '\n')
