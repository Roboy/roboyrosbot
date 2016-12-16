import sys, time, telepot, os

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if(len(msg["entities"]) > 0 and msg["entities"][0]["type"] == "bot_command"):
        cmd,args = msg["text"].split(" ")[0]
        if cmd == "/connect":
            print(args)
            ros_connect(args)

TOKEN = ""

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

while 1: time.sleep(1)
