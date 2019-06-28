# Home-IP-Getter
Telegram bot that retrieves your home IP

The idea of this is to create a Telegram bot that will get my home IP and send it to myself as a Telegram message.

This is useful for people who have a Dynamic IP where their IP may change regularly. I wrote this so that I can have access to my home Raspberry Pi server and home network no matter where I am.

# Features
This bot has basic access control so that only certain Telegram user handles have access.

# Configuration
APIKEY - Add your APIKEY here (Get it from BotFather)
IP_API_SERVICE - URL for the API you want to use to retrieve your IP address (Default: 'https://api.ipify.org')
TELEGRAM USERNAME - List of Username strings you would like to allow access. Leave blank if you want to allow all
