import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("5909685271:AAGrx4Ghfrwvw_J9DH2WS2nXLjAjLF6BrTM")

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("29409646"))
    API_HASH = os.environ.get("a69d0340a520c1913c517bea143a3de7")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5564974530").split())

    # Ban Unwanted Members..
    BANNED_USERS = []

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Generate screenshots for file after uploading
    # Defaults to True
    SCREENSHOTS = os.environ.get("SCREENSHOTS", "True")

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600

    # watermark file
    DEF_WATER_MARK_FILE = "@SK_MoviesOffl"

    # Sql Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Test:1234@cluster0.2bzsp0q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
