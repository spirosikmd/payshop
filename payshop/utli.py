from payshop import app


def change_href_from_response(response):
    key = 'href'
    if key in response:
        parts = response[key].split('/')
        parts[0] = 'http:'
        parts[2] = '{host}:{port}'.format(host=app.config['HOST'], port=app.config['PORT'])
        response[key] = '/'.join(parts)
    for k, v in response.items():
        if isinstance(v, dict):
            change_href_from_response(v)
        elif isinstance(v, list):
            for d in v:
                change_href_from_response(d)
    return response
