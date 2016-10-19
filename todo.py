import requests
import sys
import json

TRELLO_BOARD_URL = ("https://api.trello.com/1/boards/{boardid}"
                    "?lists=open&list_fields=name&fields=name,desc"
                    "&key={key}&token={token}")
TRELLO_LIST_URL = ("https://api.trello.com/1/lists/{listid}?fields=name"
                   "&cards=open&card_fields=name"
                   "&key={key}&token={token}")

config = json.loads(open('config.json').read())
list_name = sys.argv[1]

boarddata = requests.get(TRELLO_BOARD_URL.format(
    boardid=config['board_id'],
    key=config['api_key'],
    token=config['app_token'],
)).json()

for l in boarddata['lists']:
    if list_name == l['name']:
        listid = l['id']
        listdata = requests.get(TRELLO_LIST_URL.format(
            listid=listid,
            key=config['api_key'],
            token=config['app_token'],
        )).json()
        print(':: {} ::'.format(list_name))
        for item in listdata['cards']:
            print('* {}'.format(item['name']))
