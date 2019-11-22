from examples import config
import swagger_client
from swagger_client.rest import ApiException


client = swagger_client.ApiClient(config.get())

serving_api = swagger_client.api.serving_api.ServingApi(client)

serving_workspace_name, serving_name = 'expo-recall', 'demo-0-0-1'

try:
    print(f'Trying to disable serving {serving_workspace_name}/{serving_name}...')
    serving = serving_api.serving_disable(serving_workspace_name, serving_name)
    print(f'Serving successfully disabled')
except ApiException as e:
    print('Error when disable serving: %s\n' % e)

try:
    print(f'Trying to enable serving {serving_workspace_name}/{serving_name}...')
    serving = serving_api.serving_enable(serving_workspace_name, serving_name)
    print(f'Serving successfully enabled')
except ApiException as e:
    print('Error when enable serving: %s\n' % e)
