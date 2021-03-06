import requests

from flask import (
    Blueprint,
    jsonify,
)
from payshop import app
from payshop.utli import change_href_from_response

__resource__ = 'events'

mod_event = Blueprint('event', __name__, url_prefix='/{resource}'.format(resource=__resource__))


@mod_event.route('', methods=['GET'])
def events():
    events_url = '{shopping_service_base_url}/{resource}'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'],
        resource=__resource__)
    response = requests.get(
        url=events_url,
        auth=app.config['AUTH'],
        headers=app.config['HEADERS'])
    json_response = change_href_from_response(response.json())
    return jsonify(json_response)


@mod_event.route('/<event_uid>', methods=['GET'])
def event(event_uid):
    events_url = '{shopping_service_base_url}/{resource}/{event_uid}'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'],
        resource=__resource__,
        event_uid=event_uid)
    response = requests.get(
        url=events_url,
        auth=app.config['AUTH'],
        headers=app.config['HEADERS'])
    json_response = change_href_from_response(response.json())
    return jsonify(json_response)
