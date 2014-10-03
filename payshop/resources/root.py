import requests

from flask import (
    Blueprint,
    jsonify,
)
from payshop import app

mod_root = Blueprint('root', __name__, url_prefix='/')


@mod_root.route('', methods=['GET'])
def root():
    root_url = '{base_url}'.format(base_url=app.config['SHOPPING_SERVICE_BASE_URL'])
    response = requests.get(root_url, auth=app.config['AUTH'], headers=app.config['HEADERS'])
    return jsonify(response.json())
