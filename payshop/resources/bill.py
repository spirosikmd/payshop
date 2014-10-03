import requests

from flask import (
    Blueprint,
    jsonify,
    request,
)
from payshop import app

__resource__ = 'bill'

mod_bill = Blueprint('bill', __name__, url_prefix='/{resource}'.format(resource=__resource__))


@mod_bill.route('', methods=['GET'])
def bill():
    bill_url = '{shopping_service_base_url}/{resource}'.format(
        shopping_service_base_url=app.config['SHOPPING_SERVICE_BASE_URL'],
        resource=__resource__)
    headers = {'content-type': 'application/json'}
    response = requests.get(bill_url, auth=app.config['AUTH'], params=request.args, headers=headers)
    return jsonify(response.json())
