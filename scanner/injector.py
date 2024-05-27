import requests
from urllib.parse import urlencode

def load_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def inject_payloads(url, method, params, payloads):
    for payload in payloads:
        test_params = params.copy()
        for key in test_params:
            test_params[key] = payload

        if method == 'get':
            full_url = f"{url}?{urlencode(test_params)}"
            response = requests.get(full_url)
        else:  # method == 'post'
            response = requests.post(url, data=test_params)

        if payload in response.text:
            return True, payload

    return False, None
