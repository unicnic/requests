
import requests
import os


class YaUploader:
    host = 'https://cloud-api.yandex.net'
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }


    def get_upload_link(self, file_name):
        uri = '/v1/disk/resources/upload/'
        url = self.host + uri
        params = {'path': f'{file_name}'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload(self, path_to_file: str):
        file_name = os.path.basename(path_to_file)
        result = requests.put(self.get_upload_link(file_name), headers=self.get_headers(), data=open(path_to_file, 'rb'))



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь к файлу: ')
    TOKEN = input('Введите токен: ')
    uploader = YaUploader(TOKEN)
    result = uploader.upload(path_to_file)

