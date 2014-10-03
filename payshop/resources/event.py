import requests

from flask import (
    Blueprint,
    jsonify,
)
from payshop import app

mod_event = Blueprint('event', __name__, url_prefix='/events')


@mod_event.route('/', methods=['GET'])
def event_list():
    events_url = '{shopping_service_base_url}/events'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'])
    headers = {'content-type': 'application/json'}
    response = requests.get(events_url, auth=app.config['AUTH'], headers=headers)
    return jsonify(response.json())


@mod_event.route('/<event_uid>', methods=['GET'])
def event(event_uid):
    events_url = '{shopping_service_base_url}/events/{event_uid}'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'],
        event_uid=event_uid)
    headers = {'content-type': 'application/json'}
    response = requests.get(events_url, auth=app.config['AUTH'], headers=headers)
    return jsonify(response.json())
