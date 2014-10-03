import requests

from flask import (
    Blueprint,
    jsonify,
    request,
)
from payshop import app

__resource__ = 'products'

mod_product = Blueprint('product', __name__, url_prefix='/{resource}'.format(resource=__resource__))


@mod_product.route('', methods=['GET'])
def products():
    products_url = '{shopping_service_base_url}/{resource}'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'],
        resource=__resource__)
    headers = {'content-type': 'application/json'}
    response = requests.get(products_url, auth=app.config['AUTH'], params=request.args, headers=headers)
    return jsonify(response.json())


@mod_product.route('/<product_uid>', methods=['GET'])
def product(product_uid):
    product_url = '{shopping_service_base_url}/{resource}/{product_uid}'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'],
        resource=__resource__,
        product_uid=product_uid)
    headers = {'content-type': 'application/json'}
    response = requests.get(product_url, auth=app.config['AUTH'], headers=headers)
    return jsonify(response.json())
