from requests import get
import config

def get_IP_address():
    ip = get(config.IP_API_SERVICE).text
    return ip

