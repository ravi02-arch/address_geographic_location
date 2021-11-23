from flask import Flask

from app.blueprints.get_address_details import address_details

APP = Flask(__name__)

APP.register_blueprint(address_details)
