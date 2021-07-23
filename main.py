import time
from datetime import datetime

print('https://replit.com/@Levashov/messenger')

# None
# True False
# 1
# 1.5
# '123'
# l = [1, 2, 3, 'hello', [0, 1, 3]]
# {'text': 'hello', 'name': 'Jack', 'time': '15.09.2020 14:15:00'}

# def pow(a, b):
#     r = a ** b
#     print(a, '**', b, '=', r)
#     return r

# pow(10, 3)
# pow(5, 6)
# pow(9, 100)


# 1) Database
db = [
    {
        'text': 'hello',
        'name': 'Jack',
        'time': time.time()
    },
    {
        'text': 'hello, Jack',
        'name': 'John',
        'time': time.time()
    }
]

# 2) send_message

def send_message(text, name):
    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)


# 3) get_messages

def get_messages(after):
    result = []

    for message in db:
        if message['time'] > after:
            result.append(message)

    return result


# messages = get_messages(0)

def print_messages(messages):
    for message in messages:
        print(datetime.fromtimestamp(message['time']), message['name'])
        print(message['text'])
        print()
    print('-' * 50)


print_messages(db)
send_message('Привет', 'Борис')
send_message('Привет, Борис', '123')
print_messages(db)
