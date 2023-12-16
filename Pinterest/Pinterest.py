import requests
import os
import time

from requests import Response
from json import dumps
from threading import Thread

from Pinterest.helpers import Datetime, logging

class Pinterest:
    def __init__(self) -> None:
        self.__BASE_URL: str = 'https://www.pinterest.com'
        self.__datetime: Datetime = Datetime()
        self.__result: dict = {}
        
        self.__result['date_now']: str = None
        self.__result['keyword']: str = None
        self.__result['size']: str = None
        self.__result['data']: list = []

    def __build_params(self, keyword: str, size: int) -> dict:
        return {
            'data': dumps({
                "options": {
                    "article": "",
                    "appliedProductFilters": "---",
                    "price_max": None,
                    "price_min": None,
                    "query": keyword,
                    "scope": "pins",
                    "auto_correction_disabled": "",
                    "top_pin_id": "",
                    "filters": "",
                    "page_size": size
                },
                "context": {}
            })
        } 
    
    def __filter_data(self, datas: list, download: bool, output: str) -> None:
        self.__result['size'] = len(datas)

        for data in datas:
            logging.info(f'Extract data with id {data["id"]}')

            if(download): Thread(target=self.__download, args=(data["images"]["orig"]["url"], output)).start()

            self.__result['data'].append({
                "id": data["id"],
                "created_at": self.__datetime.execute(data["created_at"]),
                "domain": data["domain"],
                "link_pin": f'{self.__BASE_URL}/pin/{data["id"]}',
                "link": data["link"],
                "title": data["title"],
                "description": data["description"],
                "media": {
                    "images": data["images"],
                    "videos": data["videos"]
                }
            })

    def __download(self, url: str, output: str) -> None:
        response: Response = requests.get(url)

        logging.info(f'Download image with name {url.split("/")[-1]}')

        if(not os.path.exists(output)):
            os.makedirs(output)

        with open(f'{output}/{url.split("/")[-1]}', 'wb') as file:
            file.write(response.content)

    def search(self, keyword: str, **kwargs):
        size = kwargs.get('size', 10)
        download = kwargs.get('download', False)
        output = kwargs.get('output', 'data')

        logging.info(f'searching with key {keyword}')

        response: Response = requests.get(f'{self.__BASE_URL}/resource/BaseSearchResource/get', params=self.__build_params(keyword, size if size < 250 else 250))

        if(response.status_code != 200): return logging.error(f'failed searching with key {keyword}')

        self.__result['date_now']: str = self.__datetime.now()
        self.__result['keyword']: str = keyword

        self.__filter_data(response.json()['resource_response']['data']['results'], download, f'{output}/{keyword}')

        return self.__result

# testing
if(__name__ == '__main__'):
    start = time.perf_counter()

    pins = Pinterest = Pinterest()
    pins.search('freya', size=250)
    # with open('test_data2.json', 'w') as file:
    #     file.write(dumps(self.__result, indent=2, ensure_ascii=False))

    print(time.perf_counter() - start)

# pagging berdasarkan bookmarks