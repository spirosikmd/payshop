# Statement for enabling the development environment.
DEBUG = True

# Define the application directory.
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# The base URL of the shopping service API.
SHOPPING_SERVICE_BASE_URL = 'https://shopping-service.sandbox.paylogic.com'

# The api key that allows access to the shopping service API.
API_KEY = ''

# The api secret that grants access to shopping service API.
API_SECRET = ''
