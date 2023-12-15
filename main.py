import requests

url = 'https://www.pinterest.com/resource/BaseSearchResource/get/?source_url=/search/pins/?q=freya&rs=typed&data={"options":{"article":"","appliedProductFilters":"---","price_max":null,"price_min":null,"query":"freya","scope":"pins","auto_correction_disabled":"","top_pin_id":"","filters":"","page_size":"14"},"context":{}}&_=1702623698442'

params = {
    "source_url":"/search/pins/?q=ashel",
    "rs": "typed",
    "data": '{"options":{"article":"","appliedProductFilters":"---","price_max":null,"price_min":null,"query":"ashel","scope":"pins","auto_correction_disabled":"","top_pin_id":"","filters":"","page_size":"14"},"context":{}}',
    "_": 1702623698442
}

res = requests.get('https://www.pinterest.com/resource/BaseSearchResource/get', params=params)

print(res.json()['resource_response']['data']['results'].pop()['images'])