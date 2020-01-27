from examples import config
import kclient
from kclient.rest import ApiException
from kclient.utils import client

cl = client.with_bearer_token(config.bearer_token())
inference_api = kclient.api.inference_api.InferenceApi(cl)

workspace_name, catalog_inference_name, version = 'kuberlab-demo', 'demo', '0.0.1'
try:
    print(f'Trying to read inference version {workspace_name}/{catalog_inference_name}:{version}...')
    version_info = inference_api.inference_inference_version_info(workspace_name, catalog_inference_name, version)
    print(f'Inference version successfully read')
except ApiException as e:
    print('Error when calling inference version info: %s\n' % e)
