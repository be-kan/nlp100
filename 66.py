import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.artists
collection = db.artists

print(collection.find({'area': 'Japan'}).count())
