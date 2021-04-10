import json as j
from time import sleep
import html2text as h
import requests as r
import os, vk, vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.utils import get_random_id

api_token = os.environ["APITOKEN"]
lp_key = os.environ["LPKEY"]
authors = os.environ["AUTHORS"]
group_id = os.environ["GROUPID"]
delay = int(os.environ["DELAY"])
chat = os.environ["CHAT"]

lp_server = "https://lp.vk.com/wh"+str(group_id)
rest_posts = "https://w41k3r.com/wp-json/wp/v2/posts?author="
ids = {"50949": "#t34m474n",
       "26469": "#t34m474n",
       "5029": "#0",
       "4637": "#0"}

def send_message(text):
    vk.messages.send(
        key=lp_key,
        server=lp_server,
        ts="1",
        random_id=get_random_id(),
        message=text,
        chat_id=chat,
    )

def render_msg(content):
    text = h.html2text(content["content"]["rendered"])
    title = h.html2text(content["title"]["rendered"])
    url = content['link']
    wid = str(content["author"])
    text = text.replace("\n\n", "\n").replace("![]", "")
    if wid in ids: author = ids[wid]
    else: author = "#" + wid
    msg = "Новый пост от " + author + " -\n" \
          + title + text + "\nСсылка на пост: " + url
    return msg

def parse_user_posts(ids):
    global old_post_ids
    new_post_ids = []
    page = s.get(rest_posts + ids)
    parsed = j.loads(page.text)
    for i in parsed:
        new_post_ids.append(i["id"])
        if not i["id"] in old_post_ids:
            out = render_msg(i)
            send_message(out)
            print(out)
    old_post_ids = new_post_ids

vk_session = vk_api.VkApi(token=api_token)
longpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()
s = r.session()
old_ids = []
old_post_ids = []
old_comm_ids = []

while True:
    parse_user_posts(authors)
    sleep(delay)
