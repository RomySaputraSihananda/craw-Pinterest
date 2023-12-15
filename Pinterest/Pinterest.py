import requests
from requests import Response
from json import dumps
from Pinterest.helpers import Datetime

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
    
    def __filter_data(self, datas: list) -> None:
        self.__result['size'] = len(datas)

        for data in datas:
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

    def search(self, keyword: str, **kwargs):
        size = kwargs.get('size', 10)

        response: Response = requests.get(f'{self.__BASE_URL}/resource/BaseSearchResource/get', params=self.__build_params(keyword, size)).json()

        self.__result['date_now']: str = self.__datetime.now()
        self.__result['keyword']: str = keyword

        self.__filter_data(response['resource_response']['data']['results'])

        with open('test_data2.json', 'w') as file:
            file.write(dumps(self.__result, indent=2, ensure_ascii=False))

# testing
if(__name__ == '__main__'):
    pins = Pinterest = Pinterest()
    pins.search('freya', size=5)