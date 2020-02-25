import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


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
    return True


def friends_list(acct):
    """
    (str) -> list
    Sends request to Twitter and returns user's friends list.
    """
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '20'})
    print('Retrieving', url)
    try:
        connection = urllib.request.urlopen(url, context=ctx)
    except:
        return []
    data = connection.read().decode()
    js = json.loads(data)
    return js['users']
