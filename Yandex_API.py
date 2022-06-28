import json
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                        'Authorization': f'OAuth {self.token}'}
        self.params = {'path': folder}

    def create_folder(self, folder: str):
        result = requests.put(self.url, headers=self.headers, params=self.params)
        status_get = requests.get(self.url, headers=self.headers, params=self.params)
        return result.status_code, status_get.status_code


tokenYA = ''
folder = 'backup'


