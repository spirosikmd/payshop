import requests

from flask import (
    Blueprint,
    jsonify,
    request,
)
from payshop import app

__resource__ = 'orders'

mod_order = Blueprint('order', __name__, url_prefix='/{resource}'.format(resource=__resource__))


@mod_order.route('', methods=['POST'])
def orders():
    orders_url = '{shopping_service_base_url}/{resource}'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'],
        resource=__resource__)
    headers = {'content-type': 'application/json'}
    response = requests.post(orders_url, auth=app.config['AUTH'], data=request.data, headers=headers)
    return jsonify(response.json())


@mod_order.route('/<order_uid>', methods=['GET'])
def order(order_uid):
    order_url = '{shopping_service_base_url}/{resource}/{order_uid}'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'],
        resource=__resource__,
        order_uid=order_uid)
    headers = {'content-type': 'application/json'}
    response = requests.get(order_url, auth=app.config['AUTH'], headers=headers)
    return jsonify(response.json())
