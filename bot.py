import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import pave_event_space, per_chat_id, create_open
import logging
from logging.handlers import TimedRotatingFileHandler

import config as cf
import ipget

def getLogger():
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    fileHandler = TimedRotatingFileHandler(cf.LOG_PATH + cf.FILE_NAME,when="d",interval=1,backupCount=30)
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)
    return logger

logger = getLogger()

logger.info('Starting up Telegram bot server...')
logger.info('Current IP is: ' + ipget.get_IP_address())

class MessageCounter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(*args, **kwargs)

    def on_chat_message(self, msg):
        
        user = msg['chat']['username']
        if 'text' in msg:
            message = msg['text']
        else:
            message = "blank"
        logger.info("Received message from: " + user + " - Message: " + message)

        if user.lower() in cf.TELEGRAM_USERNAME or not cf.TELEGRAM_USERNAME:
            # Accept user
            self.sender.sendMessage("Your IP is: " + ipget.get_IP_address())
            logger.info(user + " successfully acquired IP address")

        else:
            # Deny user
            self.sender.sendMessage("You are not authorised to get the IP.")
            logger.info(user + " attempted to use the bot")
                	
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

