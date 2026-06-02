import re
import os
import time
import datetime

id_pattern = re.compile(r"^.\d+$")


class Config:

    # Telegram Bot
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = ":memory:"

    # Telegram API
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH")

    # Google OAuth / YouTube
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    # Bot Owner
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "8036555271"))

    # Bot Start Time
    BOT_START_TIME = time.time()
    BOT_START_DATETIME = datetime.datetime.now().strftime(
        "%B %d, %Y %I:%M:%S %p"
    )

    # Database
    DB_NAME = os.environ.get("DB_NAME", "Utubeitbot")
    DB_URL = os.environ.get("DB_URL")

    # Support
    SUPPORT_CHAT_LINK = os.environ.get("SUPPORT_CHAT_LINK")

    # Authorized Users
    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [
            int(user.strip())
            for user in AUTH_USERS_TEXT.split(",")
            if user.strip().isdigit()
        ]
        if AUTH_USERS_TEXT
        else []
    )

    # Video Settings
    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "")
        .replace("<", "")
        .replace(">", "")
    )

    VIDEO_CATEGORY = int(
        os.environ.get("VIDEO_CATEGORY", 0)
    )

    VIDEO_TITLE_PREFIX = os.environ.get(
        "VIDEO_TITLE_PREFIX", ""
    )

    VIDEO_TITLE_SUFFIX = os.environ.get(
        "VIDEO_TITLE_SUFFIX", ""
    )

    # Debug
    DEBUG = os.environ.get(
        "DEBUG", "False"
    ).lower() == "true"

    # Upload Mode
    UPLOAD_MODE = os.environ.get("UPLOAD_MODE", "").lower()

    if UPLOAD_MODE not in [
        "private",
        "public",
        "unlisted",
    ]:
        UPLOAD_MODE = False

    # Credential File
    CRED_FILE = "auth_token.txt"
