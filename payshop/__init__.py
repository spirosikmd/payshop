# Import flask and template operators
from flask import Flask

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
app.config.from_envvar('PAYSHOP_SETTINGS')

#
app.config['AUTH'] = app.config['API_KEY'], app.config['API_SECRET']

# Setup a global headers.
app.config['HEADERS'] = {
    'content-type': 'application/json',
}

# Import a module / component using its blueprint handler variable (mod_auth)
from payshop.resources.root import mod_root
from payshop.resources.event import mod_event
from payshop.resources.product import mod_product
from payshop.resources.bill import mod_bill
from payshop.resources.order import mod_order

# Register blueprint(s)
app.register_blueprint(mod_root)
app.register_blueprint(mod_event)
app.register_blueprint(mod_product)
app.register_blueprint(mod_bill)
app.register_blueprint(mod_order)
