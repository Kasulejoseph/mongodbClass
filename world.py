import bottle

@bottle.route('/')
def index():
    mythings = ['apple', 'orange', 'banana', 'peach']
    #return bottle.template('hello_world',username="kasule", things=mythings)
    return bottle.template('hello_world',{'username':'joseph','things':mythings})

bottle.debug(True)
bottle.run(host='localhost', port=8080)
    