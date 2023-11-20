import vk_api.exceptions

from utils import (
    get_groups_list, sort_groups, output_top_groups, write_file
)


if __name__ == '__main__':
    try:
        user_id = int(input('enter user id, only numbers without "id": '))
        quantity = int(input('enter quantity groups: '))
        groups_list = get_groups_list(user_id)
        sorted_list = sort_groups(groups_list)
        output_top = output_top_groups(sorted_list, quantity)
        write_file(output_top, user_id)
    except ValueError:
        print("Input only numbers!!!")
    except vk_api.exceptions.ApiError:
        print("This profile is deleted, banned or private")
