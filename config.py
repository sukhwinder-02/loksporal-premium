import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")


BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Backbenchers1Bot")
BAN = int(os.environ.get("BAN", "498459845"))
DELETE_AFTER = int(os.environ.get("DELETE_AFTER", 600)) #seconds
NOTIFICATION_TIME = int(os.environ.get('NOTIFICATION_TIME', 600)) #seconds
AUTO_DELETE = os.environ.get("AUTO_DELETE", True) #ON/OFF
DELETE_INFORM = os.environ.get("INFORM" , "0")
NOTIFICATION = os.environ.get("NOTIFICATION" ,f"ᴛʜɪꜱ ꜰɪʟᴇ ᴡɪʟʟ ʙᴇ  ᴅᴇʟᴇᴛᴇᴅ ɪɴ 10 mins.")
GET_INFORM = os.environ.get("GET_INFORM" , "File was deleted after {DELETE_AFTER} seconds. Use the button below to GET FILE AGAIN.")



#Your API ID & API HASH from my.telegram.org [https://youtu.be/gZQJ-yTMkEo?si=H4NlUUgjsIc5btzH]
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20125084"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0abf00cabd6805a2445181af2458571c")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002480090713"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "8054660342"))

#Port
PORT = os.environ.get("PORT", "8585")

#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Back:benchers@cluster0.z8elp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Back")

#Shortner (token system) 
# check my discription to help by using my refer link of shareus.io
# 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "shortxlinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "beee7ca2a1a57594f173b6c0153bed7f38a55434")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/OttSandhu") # shareus ka tut_vid he 

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002494488886"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002480090713"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", True)
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("<b>ʜᴇʏ</b> <a href='tg://user?id={id}'><b>{first}</b></a>\n\n<b>ɪ ᴀᴍ ᴀ ᴘᴇʀᴍᴇɴᴀɴᴛ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ ᴀɴᴅ ᴜꜱᴇʀꜱ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ꜱᴛᴏʀᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ʙʏ ᴜꜱɪɴɢ ᴀ ꜱʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ɢɪᴠᴇɴ ʙʏ ᴍᴇ</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "8054660342 5566931950").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hello\n\nYou need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We LeakHubd or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "False" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙʀᴏ  ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴏᴡɴᴇʀ !!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @Baii_Ji"

ADMINS.append(OWNER_ID)
ADMINS.append(8054660342)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
