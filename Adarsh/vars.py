# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '16612056'))
    API_HASH = str(getenv('API_HASH', 'ae32caf162207865ff93b9b931b2ba54'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '5312383797:AAEtdwbKIZ5CM9O5p8vHACpQ80UNJmYWczY'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'Sajjad_m7981bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '6'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001797380077'))
    PORT = int(getenv('PORT', '80'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1519491952").split())  
    NO_PORT = bool(getenv('NO_PORT', 'False'))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Sajjad_m7981'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'sajad.kimo.vip')) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL', 'false'))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://king:139715202Aa@cluster0.4lzzm.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'King_network7'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
