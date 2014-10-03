import requests

from flask import (
    Blueprint,
    jsonify,
    request,
)
from payshop import app

mod_bill = Blueprint('bill', __name__, url_prefix='/bill')


@mod_bill.route('/', methods=['GET'])
def bill():
    bill_url = '{shopping_service_base_url}/bill'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'])
    headers = {'content-type': 'application/json'}
    response = requests.get(bill_url, auth=app.config['AUTH'], params=request.args, headers=headers)
    return jsonify(response.json())
