import json


def read_json(file_name):
    """
    (str) -> dict
    Returns json file as dictionary.
    """
    with open(file_name, encoding='utf-8') as file:
        data = json.load(file)
    return data


def search_user(user_id):
    """
    (str) -> bool
    If user exists returns True, otherwise returns False.
    """
    if user_id == 'abba':
        return False
    return True


def friends_list(user_id):
    """
    (str) -> list
    Sends request to Twitter and returns user's friends list.
    """
    pass
