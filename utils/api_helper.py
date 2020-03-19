import json

import requests

from utils.config import get_config


class ApiHelper:

    url = get_config('base_url_api')

    headers = {
        'Content-Type': 'application/json'
    }
    payload = {}

    def send_get_request(self, endpoint, headers=None, params=None):
        if params is None:
            params = self.payload
        if headers is None:
            headers = headers
        return requests.get(self.url + "/" + endpoint, headers=headers, params=params)

    def send_post_request(self, endpoint, headers=None, payload=None):
        if payload is None:
            payload = payload
        if headers is None:
            headers = headers
        payload = json.load(payload)
        return requests.get(self.url + "/" + endpoint, headers=headers, params=payload)
