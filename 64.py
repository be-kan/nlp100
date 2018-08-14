import json
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.artists
collection = db.artists
count = 0

with open('artist.json', 'r') as artist:
    for line in artist:
        count += 1
        jsd = json.loads(line)
        result = collection.insert_one(jsd)

        if count % 10000 == 0:
            print("%s完了！" % count)

collection.create_index([('name', pymongo.ASCENDING)])
collection.create_index([('aliases.name', pymongo.ASCENDING)])
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])

print(collection.find_one())
