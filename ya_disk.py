from pprint import pprint

import requests


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url=files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path: str, filename: str):
        response = self._get_upload_link(disk_file_path=disk_file_path)
        url = response.get("href", "")
        if url:
            response = requests.put(url=url, data=open(filename, 'rb'))
            response.raise_for_status()
            if response.status_code == 201:
                print("Success")
        else:
            print("Empty url")