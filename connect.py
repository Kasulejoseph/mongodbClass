import pymongo
from pymongo import MongoClient

#connect to database
connection = MongoClient('localhost', 27017)

db = connection.video

#handle to names collection
mo = db.movies

item = mo.find_one()

print (item['title'])