import base64
from datetime import datetime

from examples import config
import kclient
from kclient.rest import ApiException


client = kclient.ApiClient(config.get())

serving_api = kclient.api.serving_api.ServingApi(client)

serving_workspace_name, serving_name, port, model = 'expo-recall', 'demo-0-0-1', '9000', 'any'

try:
    print(f'Trying to send data to serving {serving_workspace_name}/{serving_name}...')
    data_string = 'current datetime: ' + str(datetime.now())
    data_int = 42
    data_float = 3.1415926
    data_image = 'clover.png'
    with open(data_image, "rb") as image_file:
        data_image_encoded = base64.b64encode(image_file.read()).decode()
    resp = serving_api.serving_tf_proxy_model(model, {
        'raw_input': True,
        'options': {
            'noCache': True
        },
        'inputs': {
            'test_text': {
                'data': base64.b64encode(bytes(data_string, 'utf-8')).decode(),
                'dtype': 7  # DT_STRING
            },
            'test_image': {
                'data': data_image_encoded,
                'dtype': 7  # DT_STRING
            },
            'test_int': {
                'data': data_int,
                'dtype': 9  # DT_INT64
            },
            'test_float': {
                'data': data_float,
                'dtype': 2  # DT_DOUBLE
            },
        }
    }, serving_workspace_name, serving_name, port)
    print(f'Response type: {type(resp)}')
    print('Response: ', resp)
except ApiException as e:
    print('Error when sending data serving: %s\n' % e)
