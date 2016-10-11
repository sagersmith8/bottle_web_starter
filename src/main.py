from jinja2 import Environment, FileSystemLoader
from bottle import route, run
import bottle


JINJA_ENV = Environment(
    loader=FileSystemLoader('/templates/'),
    extensions=['jinja2.ext.autoescape']
)

@route('/hi/<name>')
def say_hi(name):
    respond('hi.html',
    	{
	    'name': name
	})


@route('/static/<asset:path>')
def serve_asset(asset):
    return bottle.static_file(asset, root='static/')

def respond(templtae_file, params):
    tpl = JINJA_ENV.get_template(template_file)
    return tp.render(**params)

run(host='localhost', port='8080', debug=True)
