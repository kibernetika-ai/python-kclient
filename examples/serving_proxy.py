from examples import config
import swagger_client
from swagger_client.rest import ApiException


client = swagger_client.ApiClient(config.get())

serving_api = swagger_client.api.serving_api.ServingApi(client)

serving_workspace_name, serving_name, port, model = 'expo-recall', 'demo-0-0-1', '9000', 'any'

try:
    print(f'Trying to read serving {serving_workspace_name}/{serving_name}...')
    a, b, c = serving_api.serving_tf_proxy_model_with_http_info(model, {
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
    print(a)
    # print(f'Serving successfully read')
except ApiException as e:
    print('Error when reading serving: %s\n' % e)
