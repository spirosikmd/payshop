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
    response = requests.get(
        url=bill_url,
        auth=app.config['AUTH'],
        params=request.args,
        headers=app.config['HEADERS'])
    return jsonify(response.json())
