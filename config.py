"""
Set up the config for the request handler
"""


def config():
    config = {}
    config['webapp2_extras.sessions'] = {
        'secret_key': ''  # use secret key
    }
    return config
