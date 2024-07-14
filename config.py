from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "25062134"))
    API_HASH = environ.get("API_HASH", "1c2c6d7244d4576b2baab88337b1233a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7016509767:AAHGyELmvA9D6uCz2yPsI5sL4gr7pooU1lI") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://fowardbot:fowardbot@cluster0.qjwunlh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6302921275').split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
