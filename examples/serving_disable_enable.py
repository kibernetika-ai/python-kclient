from examples import config
import kclient
from kclient.rest import ApiException
from kclient.utils import client

cl = client.with_bearer_token(config.bearer_token())
serving_api = kclient.api.serving_api.ServingApi(cl)

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
