import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.artists
collection = db.artists

print(list(collection.find({'name': 'Queen'})))
