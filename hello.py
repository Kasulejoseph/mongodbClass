import pymongo
import bottle
from pymongo import MongoClient

@bottle.route('/')
def index():
    #connect to database
    connection = MongoClient('localhost', 27017)

    db = connection.video

    #handle to names collection
    mo = db.movies

    item = mo.find_one()
    return 'hello %s' %item['title']

@bottle.route('/test_page')
def test():
    return "this the route for test"
bottle.debug = True
bottle.run(host='localhost', port=8082)