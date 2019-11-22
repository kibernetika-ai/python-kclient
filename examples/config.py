import swagger_client


def get():
    cfg = swagger_client.Configuration()
    cfg.api_key['Authorization'] = 'aa54b182-cc2f-490e-8371-443d975f0519'
    cfg.api_key_prefix['Authorization'] = 'Bearer'
    # cfg.debug = True
    return cfg
