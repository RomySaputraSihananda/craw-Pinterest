import requests
from requests import Response
from json import dumps
class Pinterest:
    def __init__(self) -> None:
        self.__url: str = 'https://www.pinterest.com/resource/BaseSearchResource/get'
        self.__result: dict = {}
    
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

    def search(self, keyword: str, **kwargs):
        response: Response = requests.get(self.__url, params=self.__build_params(keyword, kwargs.get('size', 10)))



        # with open('test_data.json', 'w') as file:
        #     file.write(dumps(response.json()['resource_response']['data']['results'], indent=2, ensure_ascii=False))

# testing
if(__name__ == '__main__'):
    pins = Pinterest = Pinterest()
    pins.search('freya', size=12)