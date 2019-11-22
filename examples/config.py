import os

import kclient


def get():
    cfg = kclient.Configuration()
    auth = os.environ.get('KCLIENT_AUTH')
    # cfg.host = 'http://localhost:8082'
    if not auth:
        raise RuntimeError('env var KCLIENT_AUTH not set\nyou should run:\nexport KCLIENT_AUTH=XXXX')
    cfg.api_key['Authorization'] = auth
    cfg.api_key_prefix['Authorization'] = 'Bearer'
    cfg.debug = bool(os.environ.get('KCLIENT_DEBUG'))
    return cfg
