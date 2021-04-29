import requests as r
import json as j
from time import sleep
import os, telebot

token = os.environ['TELEGRAM_TOKEN']
channel = os.environ['CHANNEL_ID']
url = "http://check.ege.edu.ru/api/region"
reg = os.environ['REG']

s = r.session()
code_found = False
bot = telebot.TeleBot(token)

def parse(data):
    found = False
    for i in data:
        if i["Id"] == reg:
            found = True
    return found

def send_msg(message):
    msg = bot.send_message(channel, message, parse_mode='Markdown', disable_web_page_preview=True)

while not code_found:
    data = j.loads(s.get(url).text)
    code_found = parse(data)
    if code_found:
        send_msg("ОПУБЛИКОВАЛИ РЕЗУЛЬТАТЫ ИТОГОВОГО СОЧИНЕНИЯ -> http://check.ege.edu.ru/")
    sleep(30)

while True:
    print("lol kek")
    sleep(600)
