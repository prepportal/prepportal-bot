from PrepPortalBot import bot
from PrepPortalBot.logging import LOGGER

LOGGER(__name__).info("client successfully initiated....")
if __name__ == "__main__":
    bot.run()
