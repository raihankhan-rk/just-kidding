import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(mongo_uri)

db = client.just_kidding
