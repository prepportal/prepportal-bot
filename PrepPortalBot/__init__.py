import sys
import time
from asyncio import get_event_loop, new_event_loop, set_event_loop
# import uvloop 

from pyrogram import Client
from PrepPortalBot import config
from PrepPortalBot.database.MongoDb import check_mongo_uri
from PrepPortalBot.logging import LOGGER


# uvloop.install()
LOGGER(__name__).info("Starting PrepPortal Bot....")
BotStartTime = time.time()


if sys.version_info[0] < 3 or sys.version_info[1] < 7:
    LOGGER(__name__).critical("""
=============================================================
You MUST need to be on python 3.7 or above, shutting down the bot...
=============================================================
""")
    sys.exit(1)

    
LOGGER(__name__).info("setting up event loop....")
try:
    loop = get_event_loop()
except RuntimeError:
    set_event_loop(new_event_loop())
    loop = get_event_loop()

    
LOGGER(__name__).info(
    r"""
_____________________________________________________
|  _____                _____           _        _  |
| |  __ \              |  __ \         | |      | | |
| | |__) | __ ___ _ __ | |__) |__  _ __| |_ __ _| | |
| |  ___/ '__/ _ \ '_ \|  ___/ _ \| '__| __/ _` | | |
| | |   | | |  __/ |_) | |  | (_) | |  | || (_| | | |
| |_|   |_|  \___| .__/|_|   \___/|_|   \__\__,_|_| |
|                | |                                |
|                |_|                                |
|___________________________________________________|   
""")


LOGGER(__name__).info("initiating the client....")
LOGGER(__name__).info("checking MongoDb URI....")
loop.run_until_complete(check_mongo_uri(config.MONGO_URI))


# https://docs.pyrogram.org/topics/smart-plugins
plugins = dict(root="PrepPortalBot/plugins")
bot = Client(
    "prepportal",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=plugins)
