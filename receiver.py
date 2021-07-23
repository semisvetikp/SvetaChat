import time
import requests
from datetime import datetime


def print_messages(messages):
    for message in messages:
        print(datetime.fromtimestamp(message['time']), message['name'])
        print(message['text'])
        print()
    print('-' * 50)

after = 0

while True:
    r = requests.get(
        'http://127.0.0.1:5000/messages',
        params={'after': after}
    )
    messages = r.json()['messages']
    if messages:
        print_messages(messages)
        after = messages[-1]['time']
	
    time.sleep(1)

