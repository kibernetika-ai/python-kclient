import os


def bearer_token():
    token = os.environ.get('KCLIENT_AUTH')
    if not token:
        raise RuntimeError('env var KCLIENT_AUTH not set\nyou should run:\nexport KCLIENT_AUTH=XXXX')
    return token
