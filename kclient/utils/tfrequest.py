import base64
import os


def make(data: dict = None, files: dict = None) -> dict:

    inputs = {}

    if data is not None:
        for k in data:
            dtype = None
            dval = None
            if type(data[k]) == str:
                dtype = 7  # DT_STRING
                dval = base64.b64encode(bytes(data[k], 'utf-8')).decode()
            elif type(data[k]) == int:
                dtype = 9  # DT_INT64
                dval = data[k]
            elif type(data[k]) == float:
                dtype = 2  # DT_DOUBLE
                dval = data[k]
            if dtype is None:
                raise ValueError(f'unsupported data type {type(data[k])}')
            inputs[k] = {
                'dtype': dtype,
                'data': dval,
            }

    if files is not None:
        for k in files:
            if not os.path.isfile(files[k]):
                raise ValueError(f'file {k} is absent')
            with open(files[k], "rb") as image_file:
                data = base64.b64encode(image_file.read()).decode()
            inputs[k] = {
                'dtype': 7,  # DT_STRING
                'data': data,
            }

    return {
        'raw_input': True,
        'options': {
            'noCache': True
        },
        'inputs': inputs,
    }
