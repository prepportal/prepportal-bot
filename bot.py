from pyrogram import Client, filters
from apscheduler.schedulers.background import BackgroundScheduler
from scraper import check_for_new_results
from config import BOT_TOKEN, API_HASH, APP_ID, CHANNEL_ID

app = Client("prepportal", bot_token=BOT_TOKEN, api_id=APP_ID, api_hash=API_HASH)


@app.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply(message.text)

def check_results1():
    print("Checking for new results")
    if res := check_for_new_results():
        for k,v in res.items():
            app.send_message(CHANNEL_ID, f"New result for {k} : {v}")
    else:
        app.send_message(CHANNEL_ID, "No new results")


scheduler = BackgroundScheduler(timezone="asia/kolkata")
scheduler.add_job(check_results1, "interval", minutes=2)
scheduler.start()
app.run()