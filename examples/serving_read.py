from examples import config
import swagger_client
from swagger_client.rest import ApiException


client = swagger_client.ApiClient(config.get())

serving_api = swagger_client.api.serving_api.ServingApi(client)

workspace_name, serving_name = 'expo-recall', 'ponchik2-2-0-0'
try:
    print(f'Trying to read serving {workspace_name}/{serving_name}...')
    serving = serving_api.serving_info(workspace_name, serving_name)
    print(f'Serving successfully read')
except ApiException as e:
    print('Error when reading serving: %s\n' % e)
