import requests

from flask import (
    Blueprint,
    jsonify,
)
from payshop import app

__resource__ = 'events'

mod_event = Blueprint('event', __name__, url_prefix='/{resource}'.format(resource=__resource__))


@mod_event.route('', methods=['GET'])
def events():
    events_url = '{shopping_service_base_url}/{resource}'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'],
        resource=__resource__)
    headers = {'content-type': 'application/json'}
    response = requests.get(events_url, auth=app.config['AUTH'], headers=headers)
    return jsonify(response.json())


@mod_event.route('/<event_uid>', methods=['GET'])
def event(event_uid):
    events_url = '{shopping_service_base_url}/{resource}/{event_uid}'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'],
        resource=__resource__,
        event_uid=event_uid)
    headers = {'content-type': 'application/json'}
    response = requests.get(events_url, auth=app.config['AUTH'], headers=headers)
    return jsonify(response.json())
