from requests import get
import config as cf

def get_IP_address():
    ip = get(cf.IP_API_SERVICE).text
    return ip

