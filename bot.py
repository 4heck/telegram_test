import requests
import misc
import json
from yobit import get_btc
from time import sleep

# https://api.telegram.org/bot1030588402:AAEhXzuHCahG8OnYKQCQivq9sCPMmjiyZbk/sendmessage?chat_id=271039922&text=hi
URL = 'https://api.telegram.org/bot' + misc.token + '/'


proxies = {'http': 'socks5://{}:{}'.format(misc.ip, misc.port),
           'https': 'socks5://{}:{}'.format(misc.ip, misc.port)}


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url, proxies=proxies, headers={'User-Agent': misc.user_agent})
    print(url)
    print(proxies)
    return r.json()


def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']

    message = {'chat_id': chat_id,
               'text': message_text}

    return message


def send_message(chat_id, text="Wait a second, please..."):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():

    while True:
        answer = get_message()
        chat_id = answer['chat_id']
        text = answer['text']

        if text == '/btc':
            send_message(chat_id, get_btc())

        sleep(2)


if __name__ == '__main__':
    main()
