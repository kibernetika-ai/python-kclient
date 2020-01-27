from datetime import datetime

from examples import config
import kclient
from kclient.rest import ApiException
from kclient.utils import request, client

cl = client.with_bearer_token(config.bearer_token())
serving_api = kclient.api.serving_api.ServingApi(cl)

serving_workspace_name, serving_name = 'expo-recall', 'demo-0-0-1'

try:
    print(f'Trying to send data to serving {serving_workspace_name}/{serving_name}...')
    data = request.make(data={
        'test_text': 'current datetime: ' + str(datetime.now()),
        'test_int': 42,
        'test_float': 3.1415926,
    }, files={
        'test_image': 'clover.png',
    })
    resp = serving_api.serving_proxy(data, serving_workspace_name, serving_name)
    print(f'Response type: {type(resp)}')
    print('Response: ', resp)
except ApiException as e:
    print('Error when sending data serving: %s\n' % e)
