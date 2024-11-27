"""
from os import getenv


API_ID = int(getenv("API_ID", "24515547"))
API_HASH = getenv("API_HASH", "0809699a061f02fbbcc1a6c4443547ee")
BOT_TOKEN = getenv("BOT_TOKEN", "7497953395:AAHVGwfHenXeBouKaMS3wpFEo2hykeGPyWE")
OWNER_ID = int(getenv("OWNER_ID", "7503180362"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7503180362").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002463397200"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002338677190"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

