import requests

from flask import (
    Blueprint,
    jsonify,
    request,
)
from payshop import app

mod_product = Blueprint('product', __name__, url_prefix='/products')


@mod_product.route('/', methods=['GET'])
def product_list():
    products_url = '{shopping_service_base_url}/products'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'])
    headers = {'content-type': 'application/json'}
    response = requests.get(products_url, auth=app.config['AUTH'], params=request.args, headers=headers)
    return jsonify(response.json())


@mod_product.route('/<product_uid>', methods=['GET'])
def product(product_uid):
    product_url = '{shopping_service_base_url}/products/{product_uid}'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'],
        product_uid=product_uid)
    headers = {'content-type': 'application/json'}
    response = requests.get(product_url, auth=app.config['AUTH'], headers=headers)
    return jsonify(response.json())
