from examples import config
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models import inference_run_serving_request


client = swagger_client.ApiClient(config.get())

inference_api = swagger_client.api.inference_api.InferenceApi(client)

workspace_name, catalog_inference_name, version, serving_name = 'expo-recall', 'ponchik2', '2.0.0', 'ponchik2-2-0-0'

start_request = inference_run_serving_request.InferenceRunServingRequest(
    name=serving_name,
    workspace_name=workspace_name,
    cluster_id='edge',
    values={
        'face_detect_threshold': 0.8,
        'head_pose_thresholds': '25,25,20',
        'test_hidden_val': 'just for test 1.0.2',
        'recognizer_model_location': '',
        'recognizer_model_bearer_key': '',
        'source': {
            'repository': 'https://github.com/kuberlab/ponchik2'
        },
        'face_detection': {
            'workspace': 'expo-recall',
            'model': 'face-detection-adas-0001',
            'version': '0.0.1'
        },
        'head_pose': {
            'workspace': 'expo-recall',
            'model': 'head-pose-estimation-adas-0001',
            'version': '0.0.1'
        },
        'facenet': {
            'workspace': 'expo-recall',
            'model': 'facenet-pretrained',
            'version': '1.0.0-vgg-openvino-cpu'
        },
        'dataset': {
            'workspace': 'expo-recall',
            'dataset': 'beauty-face',
            'version': '1.0.1'
        },
        'stream': {
            'key': 'live-old',
            'input': 'server',
            'output': 'mjpg',
            'description': 'none',
            'params': {
                'cloud_status': '3',
                'output_fps': '15'
            }
        },
        'streams':[
            {
                'key':'live',
                'input': 'server',
                'output': 'mjpg',
                'description': 'none',
                'params': {
                    'cloud_status': '3',
                    'output_fps': '15'
                }
            },
            {
                'key': 'live2',
                'input': 'server',
                'output': 'mjpg',
                'description': 'none',
                'params': {
                    'cloud_status': '3',
                    'output_fps': '15'
                }
            }
        ],
        'filter_keep': False,
        'recognizer_keep': False,
        'debug': False
    },
)
try:
    print(f'Trying to start serving {workspace_name}/{serving_name} '
          f'from catalog inference\'s version {workspace_name}/{catalog_inference_name}:{version}...')
    serving = inference_api.inference_inference_version_start(start_request, workspace_name, catalog_inference_name, version)
    print(f'Serving {serving.workspace_name}/{serving.name} successfully created')
except ApiException as e:
    print('Error when starting serving: %s\n' % e)
