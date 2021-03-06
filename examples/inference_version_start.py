from examples import config
import kclient
from kclient.rest import ApiException
from kclient.models import inference_run_serving_request
from kclient.utils import client


cl = client.with_bearer_token(config.bearer_token())
inference_api = kclient.api.inference_api.InferenceApi(cl)

workspace_name, catalog_inference_name, version = "kuberlab-demo", "demo", "0.0.1"
serving_workspace_name, serving_name = "expo-recall", "demo-0-0-1"

start_request = inference_run_serving_request.InferenceRunServingRequest(
    name=serving_name,
    workspace_name=serving_workspace_name,
    cluster_id="shared/17431",
    values={
        "params_text": "Generated in python KClient",
        "source": {"repository": "https://github.com/kibernetika-ai/demo-srv"},
    },
)
try:
    print(
        f"Trying to start serving {serving_workspace_name}/{serving_name} "
        f"from catalog inference's version {workspace_name}/{catalog_inference_name}:{version}..."
    )
    serving = inference_api.inference_inference_version_start(
        start_request, workspace_name, catalog_inference_name, version
    )
    print(f"Serving {serving.workspace_name}/{serving.name} successfully created")
except ApiException as e:
    print("Error when starting serving: %s\n" % e)


"""
Form: 

- name: source
  label: Demo serving source code
  type: git
  value:
    repository: 'https://github.com/kibernetika-ai/demo-srv'
  width: 50
- name: params_text
  label: Text passed with init params
  type: string
  value: init text
  width: 50
"""

"""
Serving config template:

config:
    replicas: 1
    restartPolicy: Never
    maxRestartCount: 0
    images:
        cpu: kuberlab/serving:latest
        gpu: kuberlab/serving:latest-gpu
    command: >-
        kserving --driver null --model-path null --hooks hook.py -o params_text="{{ .params_text }}"
    workdir: "$SRC_DIR"
    resources:
        accelerators:
            gpu: 0
        requests:
            cpu: 100m
            memory: 128Mi
        limits:
            cpu: 200m
            memory: 256Mi
    ports:
        - name: "grpc"
          port: 9000
          protocol: "TCP"
          targetPort: 9000
    sources:
        - name: src
          mountPath: /src
          gitRepo:
              {{ if .source.accountId }}accountId: "{{ .source.accountId }}"{{ end }}
              repository: "{{ .source.repository }}"
"""
