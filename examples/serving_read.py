from examples import config
import kclient
from kclient.rest import ApiException
from kclient.utils import client

cl = client.with_bearer_token(config.bearer_token())
serving_api = kclient.api.serving_api.ServingApi(cl)

serving_workspace_name, serving_name = 'expo-recall', 'demo-0-0-1'

try:
    print(f'Trying to read serving {serving_workspace_name}/{serving_name}...')
    serving = serving_api.serving_info(serving_workspace_name, serving_name)
    print(f'Serving successfully read')
except ApiException as e:
    print('Error when reading serving: %s\n' % e)
