from examples import config
import kclient
from kclient.rest import ApiException


client = kclient.ApiClient(config.get())

serving_api = kclient.api.serving_api.ServingApi(client)

serving_workspace_name, serving_name, port, model = 'expo-recall', 'demo-0-0-1', '9000', 'any'

try:
    print(f'Trying to read serving {serving_workspace_name}/{serving_name}...')
    resp = serving_api.serving_tf_proxy_model(model, {
        'raw_input': True,
        'options': {
            'noCache': True
        },
        'inputs': {
            'input': {
                'data': 'data in JSON',
                'dtype': 7
            },
        }
    }, serving_workspace_name, serving_name, port)
    print('Response: ', resp)
except ApiException as e:
    print('Error when reading serving: %s\n' % e)
