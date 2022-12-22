import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "13305226")) #optional
API_HASH = getenv("API_HASH", "8cde2475d6b0cb1162b89ebbac71a95d") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "-1001521670151").split()))
OWNER_ID = int(getenv("OWNER_ID", "-1001521670151"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://A:A@cluster0.aim6z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5047736431:AAGbF856jE9DwF7-xaUxP95EPYezRytH5tQ")
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/e0150d57b5a7d36e064a2.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "IAM ALIVE Anu kunda..///")
PM_LOGGER = getenv("PM_LOGGER", "")
LOG_GROUP = getenv("LOG_GROUP", "")
GIT_TOKEN = getenv("GIT_TOKEN", "") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAKrwzR-yPn8wTcusbu0UkeujhC6G45259rnICFwyuGsH2vLB9c0J1ddoc8BO8Vz-vppZ_CjpOlw0xnjmOg-j43bFP3dq4_jflYmNnScL3z-9UPYksK5SODRRtZ4FmOwRkEfDNC3PzDJLfdupUJwvQv1yT5G6BCAvgosAkr7tMyt7SVMpF6Ev_gfxWIFynsOJoD8EN1k2IDMlU6isKHQPzcvtjT_N3BaLTamquEypxRVxLLDwoizrRWOZLHdtQqMI5maaM0KvCTF5if5DJxpZ7p-B42ldSGbwbbaYBR4WZUbLludsfRW5lKtBXuBuRKgwSDtyl2n-DsDZDyKZVY2V-eAAAAABLAEvyAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
