import requests
from json import dumps

# data = {
#     "options": {
#         "article": "",
#         "appliedProductFilters": "---",
#         "price_max": None,
#         "price_min": None,
#         "query": "tatto anime",
#         "scope": "pins",
#         "auto_correction_disabled": "",
#         "top_pin_id": "",
#         "filters": "",
#         "page_size": "14"
#     },
#     "context": {}
# }

# {
#     "options": {
#         "article": "",
#         "appliedProductFilters": "---",
#         "price_max": null,
#         "price_min": null,
#         "query": "freya",
#         "scope": "pins",
#         "auto_correction_disabled": "",
#         "top_pin_id": "",
#         "filters":"",
#         "page_size": "14",
#         "bookmarks": [
#             "Y2JVSG81V2sxcmNHRlpWM1J5VFVad1ZsWllhR3BXYlZKNFdWVmtSMVV3TVZkalJFSlhVbTFPTkZWdGMzZGxSMHBIVm14T2FWZEhhRzlXVjNCSFpESk5lRlZzVmxSaE1sSndWbXhTVjJWR1duTlZhMDVhVm10d1IxbHJVazlYUjBwVlVtdG9XbUV4Y0ROWk1WcFhaRWRLU0ZKdGFHaE5WbGw2Vm1wR2IyUXhXbkpOVlZwT1ZsWmFjRlZxU205WlZscHlXa2M1YTFKdFVsbFpNR1F3WVZaYWRWRnJXbGhXUlRWMlZrUktWMk5yTVZWVmJGWk9VakZLV0ZaR1ZtRmtNazVYVm14V1YyRjZWbGhVVmxaM1pERmFSMVZyZEZoaGVrSXpWRlphVjFWdFNsVlNhemxhWWxSV2RsWlZXbGRqTVdSMFpFWkNVbFpFUVRWYWExcFhVMWRLTmxWck9WZE5XRUpIVm0wd2VFMUdiRmRUYTJoc1UwVktXVmxzVWtkWlZsSldWMjVPVDJKR1dsWlZNbmgzVmpBeFIyTkliRmRTYkZwVVZqSnpkMlF3TVZkV2JGSllVakZLVUZadGRGZFpWMDVYVlZob1ZtRXpRbEJXYkZKelZteGtXV05HWkZaU2EzQkhWV3hTUjFkR1duTlRiRUphWVRGV05GWXdXbUZXVmxaelVXeE9VMDFzUlhkV2FrbzBZVEZSZVZKWVpFNVhSa3BVVm10V1lXRkdiSE5YYTJSUFZteEtNRmt3YUU5aFJrcDBaSHBLVmxac1NsUldSRVphWlVaT2RWTnNhR2hOVlhCTlYxZDRWbVZIVWtkVWJrWm9VbXhhYjFSV1duZFhiR1IwWkVWYVVGWnJTbE5WUmxGNFQwVTFjVk50YUZCV1JYQnlWRmN4VGsxRk5YRmhla1pPVWtWV05GUlVTbGRoVm13MlZGaHNUbUZyTURGVWJHUkxZVlV4V0ZWVVRrNVdSVVl6VkZjeFJtVkZOVlZoUjJoYVpXMW9kRlF3WkVaT1JuQjBWMVJHVG1KV1ZURlVNRkpyWWxac2NWTllhRTVXUld3MlZHNXdhazFHY0ZsbFJUbFRWbTFSTkdaRWJHbE9WRVV6VGxSUmVFOVVUWGROTWsxNlRYcG5lVTVVVVhoYVZHTXdXVlJyZUUxVWEzbFpiVlV3VDFkT2FWbHFaelJOUkVVeFRWUkJNVTFYU1RSTmVtdDZUVzFSTVUxcVRYZE9SMWwzV1ZkWmVVOUVVamhVYTFaWVprRTlQUT09fFVIbzRORlJIU2paYWJtaFNWRmhTZUZKVU1XWk5WRWt5V0hrd2VHWkVRVE5QUkZsNFdsUkJNazlFV214WmJWbDZUVVJSZVU0eVNURlphbFUxV2tkSmVrMUVXWGhaZW1oc1QwUlJNMXB0V21wYVYwNW9UVVJKTUUxRWEzaGFWRlUwVDBkVk0xbFVVVFZhYWsxNVRsZFZkMXB0V2poVWExWllaa0U5UFE9PXxOb25lfE5vbmV8Y2M4ZmI3MTVhMGZiNmI0NDBlMjZlODZiZDk5MjUwOGQzNjE4YTBjMmM2OTkxNWQ2ODIxMTY3YjhmNjEzODhkN3xORVd8"
#         ]
#     },
#     "context":{}
# }

# params = {
#     "data": '{"options":{"article":"","appliedProductFilters":"---","price_max":null,"price_min":null,"query":"melody jkt48","scope":"pins","auto_correction_disabled":"","top_pin_id":"","filters":"","page_size":"14"},"context":{}}'
# }

data = {
    "queryHash": "b83506d70dca12d87a3ad608c5701f991b7e026e3173f50f526132be5a676d12",
    "variables": {
        "pinId": "165718461281756936",
        "isAuth": False
    }
}

res = requests.post('https://www.pinterest.com/_/graphql/', json=data)

print(res.text)

# print(len(res.json()['resource_response']['data']['results']))
# print(res.json()['resource_response']['data']['results'].pop()['images'])