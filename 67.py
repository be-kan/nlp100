import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.artists
collection = db.artists

clue = input('アーティストの別名を入力してください--> ')
print(list(collection.find({'aliases.name': clue})))
