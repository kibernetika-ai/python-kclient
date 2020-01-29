from examples import config
import kclient
from kclient.rest import ApiException
from kclient.utils import client

from kclient.utils.download import download

cl = client.with_bearer_token(config.bearer_token())
serving_api = kclient.api.serving_api.ServingApi(cl)

serving_workspace_name, serving_name, jod_id = 'steadytake', 'motdt', '9bfe92ee-001d-4ff3-acaa-9cd0763e4edc'

try:
    print(f'Trying to get job {jod_id} data from serving {serving_workspace_name}/{serving_name}...')
    resp = serving_api.serving_project_job(jod_id, serving_workspace_name, serving_name)
    print('Response: ', resp)

    try:
        output = resp.outputs[1]
        download(cl, output.link, output.file)
    except ApiException as e:
        print('Error when downloading file: %s\n' % e)

except ApiException as e:
    print('Error when getting data: %s\n' % e)

