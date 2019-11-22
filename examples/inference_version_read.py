from examples import config
import swagger_client
from swagger_client.rest import ApiException


client = swagger_client.ApiClient(config.get())

inference_api = swagger_client.api.inference_api.InferenceApi(client)

workspace_name, catalog_inference_name, version = 'expo-recall', 'ponchik2', '2.0.0'
try:
    print(f'Trying to read inference version {workspace_name}/{catalog_inference_name}:{version}...')
    version_info = inference_api.inference_inference_version_info(workspace_name, catalog_inference_name, version)
    print(f'Inference version successfully read')
except ApiException as e:
    print('Error when calling inference version info: %s\n' % e)
