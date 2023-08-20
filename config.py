import os
import dotenv

dotenv.load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
APP_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("API_HASH")
CHANNEL_ID = os.environ.get("CHANNEL_ID")