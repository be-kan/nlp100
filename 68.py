import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.artists
collection = db.artists

results = list(collection.find({'tags.value': 'dance'}).sort('rating.count', pymongo.DESCENDING))

for result in results[1:10]:
    print('-------------------------------')
    print(result)
