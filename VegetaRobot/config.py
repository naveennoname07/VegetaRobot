# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import re
import json #by ctzfamioy
import os
from os import environ

def get_user_list(config, key):
    with open('{}/VegetaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 7126006  # integer value, dont use ""
    API_HASH = "f92b05be529835381859ead64a195fa2"
    TOKEN = "2128359921:AAFo-u0Y0e3ZNh2JScMGYoe9oy2UBQuur_4"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1491497760  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "ctzfamily"
    SUPPORT_CHAT = 'vegetasupport'  #Your own group for support, do not add the @
    UPDATES_CHANNEL = 'vegetaUpdates' #Your own channel for Updates of bot, Do not add @
    JOIN_LOGGER = -1001543354286  #Prints any new group the bot is added to, prints just the name and ID.
    REM_BG_API_KEY = "dxsh728mZMDmj4ijSZCNPZig"
    STRING_SESSION = "1BVtsOIgBu2dMF7FyBJZOig7ITZDtkaJQ-9y2i_kNIP_zTcUQ5-QG-yl04x5jbZgsnIF1n8mVg8WVQbMZB8Hi5edGcQUy8NM9QXj5IILEeIHtEBs_dFMcZ0z-wKEZ4iL2tvbNyQOIqWAYGjnsR3c_-qmZCn3gnEjOWWN9HxLe3_6C7JVw2rhuVQVAR4dWWtVEjxWmnvUL32Dlp45STq92rBbzHyHhEUOMb6CJUKh7-b-1yS8vi7Yc_7KkL2ls8QFGg1s7i-paDZqZFnJrN0IyLj5WK01ZirX62Mqw7z9Ii58CETCQutPBU29Kwyp28vtvNjegZcANwgqZZN38vJ0G9TzwJTSX920="
    TEMP_DOWNLOAD_DIRECTORY = ""
    EVENT_LOGS = -1001543354286  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    SQLALCHEMY_DATABASE_URI = ''
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key -
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BOT_ID = "2128359921"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

# Bot settings
    CACHE_TIME = int(environ.get('CACHE_TIME', 300))
    USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
    PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()

# Admins, Channels & Users
    ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
    CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
    auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
    AUTH_USERS = (auth_users + ADMINS) if auth_users else []
    auth_channel = environ.get('AUTH_CHANNEL')
    auth_grp = environ.get('AUTH_GROUP')
    AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
    AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
    DATABASE_URI = environ.get('DATABASE_URI', "")
    DATABASE_NAME = environ.get('DATABASE_NAME', "")
    COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
    SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')
    P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
    IMDB = is_enabled((environ.get('IMDB', "True")), True)
    SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
    CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
    BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
    IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
    LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
    SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
    MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
    INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
    FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
    MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
    PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
    PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    STRICT_GMUTE = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    ARQ_API_URL = "http://thearq.tech/"
    ARQ_API_KEY = "FEUAAQ-IYDNKK-VTYUKD-LMMXLA-ARQ"
    CASH_API_KEY = 'awoo'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'awoo'  # Get your API key from https://timezonedb.com/api
    OPENWEATHERMAP_ID = 'awoo'
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'awoo'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
