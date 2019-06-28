import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import pave_event_space, per_chat_id, create_open
import logging

import config as cf
import ipget

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

logging.info('Starting up Telegram bot server...')
logging.info('Current IP is: ' + ipget.get_IP_address())

class MessageCounter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(*args, **kwargs)

    def on_chat_message(self, msg):
        
        message = msg['text']
        user = msg['chat']['username']
        logging.info("Received message from: " + user + " - Message: " + message)

        if user.lower() in cf.TELEGRAM_USERNAME or not cf.TELEGRAM_USERNAME:
            # Accept user
            self.sender.sendMessage("Your IP is: " + ipget.get_IP_address())
            logging.info(user + " successfully acquired IP address")

        else:
            # Deny user
            self.sender.sendMessage("You are not authorised to get the IP.")
            logging.info(user + " attempted to use the bot")
                	
TOKEN = cf.APIKEY

if not TOKEN:
    logging.critical('API Key is invalid! Bot cannot run')
    sys.exit()

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MessageCounter, timeout=10),
])
MessageLoop(bot).run_as_thread()

while 1:
    time.sleep(10)
