import swagger_client
from swagger_client import rest, models


cfg = swagger_client.Configuration()
cfg.host = 'https://dev.kibernetika.io'
cfg.api_key['Authorization'] = 'aa54b182-cc2f-490e-8371-443d975f0519'
cfg.api_key_prefix['Authorization'] = 'Bearer'
# cfg.debug = True

client = swagger_client.ApiClient(cfg)

inference_api = swagger_client.api.inference_api.InferenceApi(client)
serving_api = swagger_client.api.serving_api.ServingApi(client)

# try to read private inference's version
try:
    version_info = inference_api.inference_inference_version_info('expo-recall', 'ponchik2', '2.0.0')
    print(f'Inference version {version_info.version} successfully loaded')
except rest.ApiException as e:
    print('Error when calling inference version info: %s\n' % e)

# # try to start private inference version's serving
# start_request = models.inference_run_serving_request.InferenceRunServingRequest(
#     name='ponchik2-2-0-0-try-2',
#     workspace_name='expo-recall',
#     cluster_id='edge',
#     values={
#         'face_detect_threshold': 0.8,
#         'head_pose_thresholds': '25,25,20',
#         'test_hidden_val': 'just for test 1.0.2',
#         'recognizer_model_location': '',
#         'recognizer_model_bearer_key': '',
#         'source': {
#             'repository': 'https://github.com/kuberlab/ponchik2'
#         },
#         'face_detection': {
#             'workspace': 'expo-recall',
#             'model': 'face-detection-adas-0001',
#             'version': '0.0.1'
#         },
#         'head_pose': {
#             'workspace': 'expo-recall',
#             'model': 'head-pose-estimation-adas-0001',
#             'version': '0.0.1'
#         },
#         'facenet': {
#             'workspace': 'expo-recall',
#             'model': 'facenet-pretrained',
#             'version': '1.0.0-vgg-openvino-cpu'
#         },
#         'dataset': {
#             'workspace': 'expo-recall',
#             'dataset': 'beauty-face',
#             'version': '1.0.1'
#         },
#         'stream': {
#             'key': 'live-old',
#             'input': 'server',
#             'output': 'mjpg',
#             'description': 'none',
#             'params': {
#                 'cloud_status': '3',
#                 'output_fps': '15'
#             }
#         },
#         'streams':[
#             {
#                 'key':'live',
#                 'input': 'server',
#                 'output': 'mjpg',
#                 'description': 'none',
#                 'params': {
#                     'cloud_status': '3',
#                     'output_fps': '15'
#                 }
#             },
#             {
#                 'key': 'live2',
#                 'input': 'server',
#                 'output': 'mjpg',
#                 'description': 'none',
#                 'params': {
#                     'cloud_status': '3',
#                     'output_fps': '15'
#                 }
#             }
#         ],
#         'filter_keep': False,
#         'recognizer_keep': False,
#         'debug': False
#     },
# )
# try:
#     serving = inference_api.inference_inference_version_start(start_request, 'expo-recall', 'ponchik2', '2.0.0')
#     print(serving)
# except rest.ApiException as e:
#     print('Error when starting serving: %s\n' % e)
#
# # try to read serving
# try:
#     serving = serving_api.serving_info('expo-recall', 'ponchik2-2-0-0-try-2')
#     print(serving)
# except rest.ApiException as e:
#     print('Error when reading serving: %s\n' % e)
#
# # try to disable serving
# try:
#     serving = serving_api.serving_disable('expo-recall', 'ponchik2-2-0-0-try-2')
#     print(serving)
# except rest.ApiException as e:
#     print('Error when reading serving: %s\n' % e)
