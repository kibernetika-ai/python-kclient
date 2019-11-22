import os

import swagger_client


def get():
    cfg = swagger_client.Configuration()
    auth = os.environ.get('KCLIENT_AUTH')
    if not auth:
        raise RuntimeError('env var KCLIENT_AUTH not set\nyou should run:\nexport KCLIENT_AUTH=XXXX')
    cfg.api_key['Authorization'] = auth
    cfg.api_key_prefix['Authorization'] = 'Bearer'
    # cfg.debug = True
    return cfg
