from pyrogram import Client, filters, __version__
from apscheduler.schedulers.background import BackgroundScheduler
from scraper import check_for_new_results
from config import BOT_TOKEN, API_HASH, APP_ID, CHANNEL_ID
from datetime import datetime

app = Client("prepportal", bot_token=BOT_TOKEN, api_id=APP_ID, api_hash=API_HASH)

start_time = datetime.now()

@app.on_message(filters.command('start') & filters.private)
async def echo(client, message):
    await message.reply("Hello, weclome to PrepPortal!")

@app.on_message(filters.command('alive') & filters.private)
async def echo(client, message):
    current_time = datetime.now()
    uptime = current_time - start_time
    version = __version__
    await message.reply(f"The Bot is Alive!\nUptime: {uptime}\nVersion: {version}")

def check_results1():
    print("Checking for new results")
    if res := check_for_new_results():
        for k,v in res.items():
            app.send_message(CHANNEL_ID, f"New result for {k} : {v}")
    else:
        print("No new results")


scheduler = BackgroundScheduler(timezone="asia/kolkata")
scheduler.add_job(check_results1, "interval", minutes=2)
scheduler.start()
app.run()