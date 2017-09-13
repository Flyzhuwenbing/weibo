import pymongo

client = pymongo.MongoClient()
db = client.weibo
collection = db.comment

for data in collection.find():
    comment = data.get('comment')
    print(comment)