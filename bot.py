import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import pave_event_space, per_chat_id, create_open
import logging

import config
import ipget

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

logging.info('Starting up Telegram bot server...')

class MessageCounter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(*args, **kwargs)

    def on_chat_message(self, msg):
        print(msg)
        message = msg['text']
        user = msg['chat']['username']
        logging.info("Received message from: " + user + " - Message: " + message)
        self.sender.sendMessage(ipget.get_IP_address())
        	
TOKEN = config.APIKEY 

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MessageCounter, timeout=10),
])
MessageLoop(bot).run_as_thread()

while 1:
    time.sleep(10)
