import bottle

#display username a list of things
@bottle.route('/')
def index():
    mythings = ['apple', 'orange', 'banana', 'peach']
    #return bottle.template('hello_world',username="kasule", things=mythings)
    return bottle.template('hello_world',{'username':'joseph','things':mythings})

#get fruit and render it
@bottle.post('/favorite')
def favorite():
    fruit = bottle.request.forms.get('fruit')
    if (fruit ==None or fruit == ''):
        return "No fruit"
    bottle.response.set_cookie("fruit", fruit)
    bottle.redirect("/show_fruit")

@bottle.get('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie("fruit")
    return bottle.template('fruit',{'fruit':fruit})


bottle.debug(True)
bottle.run(host='localhost', port=8080)
    