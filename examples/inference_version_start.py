from examples import config
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models import inference_run_serving_request


client = swagger_client.ApiClient(config.get())

inference_api = swagger_client.api.inference_api.InferenceApi(client)

workspace_name, catalog_inference_name, version = 'kuberlab-demo', 'demo', '0.0.1'
serving_workspace_name, serving_name = 'expo-recall', 'demo-0-0-1'

start_request = inference_run_serving_request.InferenceRunServingRequest(
    name=serving_name,
    workspace_name=serving_workspace_name,
    cluster_id='shared/17431',
    values={
        'prefix': 'Generated in python KClient: ',
        'source': {
            'repository': 'https://github.com/kibernetika-ai/demo-srv'
        },
    },
)
try:
    print(f'Trying to start serving {workspace_name}/{serving_name} '
          f'from catalog inference\'s version {workspace_name}/{catalog_inference_name}:{version}...')
    serving = inference_api.inference_inference_version_start(start_request, workspace_name, catalog_inference_name, version)
    print(f'Serving {serving.workspace_name}/{serving.name} successfully created')
except ApiException as e:
    print('Error when starting serving: %s\n' % e)
