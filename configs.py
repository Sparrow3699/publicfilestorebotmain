# (c) @PredatorHackerzZ || @TeleRoidGroup

import os


class Config(object):
	API_ID = 27501733
	API_HASH = "687b5c7656849e9a3b125d691f824497"
	BOT_TOKEN = "6672694453:AAEznfVE1d-5dwFpFwHBOkchfViet9V8S2g"
	BOT_USERNAME = "FileStore_4GB_bot"
	DB_CHANNEL = -1001920799623
	BOT_OWNER = 5847742709
	DATABASE_URL = "mongodb+srv://srj726811:srj726811@cluster0.rvootx1.mongodb.net/?retryWrites=true&w=majority"
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = -1001997939827
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "").split(",") if id.strip()]
	ABOUT_BOT_TEXT = f"""
I'm [File Store 4GB bot](https://t.me/FileStore_4GB_bot)

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
 
🌟 **I'm [File Store 4GB bot](https://t.me/FileStore_4GB_bot)**

✨ **Powered By : [FileStorebotUpdates](https://t.me/FileStorebotUpdates)**

☀️ **Files Will Be Deleted In 10 Mins Due To Copyrights**

🌊 **Make Sure To Download (or) Forward Files Before They Deleted**


"""
