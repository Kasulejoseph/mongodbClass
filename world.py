import bottle

@bottle.route('/')
def index():
    mythings = ['apple', 'orange', 'banana', 'peach']
    #return bottle.template('hello_world',username="kasule", things=mythings)
    return bottle.template('hello_world',{'username':'joseph','things':mythings})

@bottle.post('/favorite')
def favorite():
    fruit = bottle.request.forms.get('fruit')
    if (fruit ==None or fruit == ''):
        return "No fruit"
    return bottle.template('fruit',{'fruit':fruit})
bottle.debug(True)
bottle.run(host='localhost', port=8080)
    