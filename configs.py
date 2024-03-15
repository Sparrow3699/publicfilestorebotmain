# (c) @PredatorHackerzZ || @TeleRoidGroup

import os


class Config(object):
	API_ID = 15682957
	API_HASH = "00b8b3714cee0ba2941091b7cc5578e7"
	BOT_TOKEN = "6518879488:AAFtd_jX7l-sblE7bVhU9p4Gdj47tmIan2o"
	BOT_USERNAME = "TeluguStorePro_bot"
	DB_CHANNEL = -1002102557194
	BOT_OWNER = 1098983599
	DATABASE_URL = "mongodb+srv://TeluguMoviesFilter:TeluguMoviesFilter@cluster0.tbhnl1n.mongodb.net/?retryWrites=true&w=majority"
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = -1001997939827
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
I'm [Telugu Store Pro Bot](https://t.me/TeluguStorePro_bot)

🌠 Send Me Any Video (or) File , Then I'll Save It To My Database And I'll Give Shareable Link To You....

🌌 I Will Work In Channel Too, So Add Me To A Channel With Full Admin Rights And Check My Power...

🌉 I Can Give Direct Shareable Link And Batch Shareable Link Too...

 **My Master** Will Be Broadcasting Movies Here Often , So Make Sure You Don't Block Me And Keep SupportinG Me 🥳
"""
	ABOUT_DEV_TEXT = f"""
BYE
"""
	HOME_TEXT = """
 Hi 🤗, [{}](tg://user?id={})
 
🌟 **I'm [Telugu Store Pro Bot](https://t.me/TeluguStorePro_bot)**

✨ **Powered By : [Adult Films](https://t.me/AdultFilmsPlus)**

☀️ **Files Will Be Deleted In **10 Mins** Due To Copyrights**

🌊 **Make Sure To Download (or) Forward Files Before They Deleted**


"""
