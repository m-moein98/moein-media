from bson.objectid import ObjectId
from pymongo import MongoClient

# Hash Algorythm
SECRET_KEY = "427d2a8539281bac983ec2da6f0ba910f661eb19f3a2edd693457250736c0548"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# DB Setting
client = MongoClient("127.0.0.1", 27017)
db = client.social_media
user_collection = db.User
token_collection = db.Token
