# Run a test server.
from payshop import app

app.run(
    host=app.config['HOST'],
    port=app.config['PORT'],
    debug=app.config['DEBUG']
)
