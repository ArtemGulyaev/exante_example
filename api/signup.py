import json
import requests

from conf.ulr import Url


def signup(body):
    payload = body
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    response = requests.request("POST", Url.signup, headers=headers, data=payload)
    dict_ = json.loads(str(response.text))
    return response, dict_
