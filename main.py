import requests
from json import dumps

data = {
    "options": {
        "article": "",
        "appliedProductFilters": "---",
        "price_max": None,
        "price_min": None,
        "query": "tatto anime",
        "scope": "pins",
        "auto_correction_disabled": "",
        "top_pin_id": "",
        "filters": "",
        "page_size": "14"
    },
    "context": {}
}

params = {
    "data": '{"options":{"article":"","appliedProductFilters":"---","price_max":null,"price_min":null,"query":"melody jkt48","scope":"pins","auto_correction_disabled":"","top_pin_id":"","filters":"","page_size":"14"},"context":{}}'
}

res = requests.get('https://www.pinterest.com/resource/BaseSearchResource/get', params={"data": dumps(data)})

print(len(res.json()['resource_response']['data']['results']))
print(res.json()['resource_response']['data']['results'].pop()['images'])