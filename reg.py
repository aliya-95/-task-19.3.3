import json

import requests

base_url = 'https://petstore.swagger.io/v2'

# GET Logs user into rhe system
status = 'available'

username = 'Aliya'
password = '81@2567'

res = requests.get(f'{base_url}/user/login?login={username}&password={password}', headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

#POST Add a new pet to the store

body = {"id": 10,
        "category": {"id": 10, "name": "Alex"},
        "name": "dog",
        "photoUrls": ['string'],
        "tags": [{"id": 11, "name": "Dog1"}],
        "status": "available"}

res = requests.post(url=f'https://petstore.swagger.io/v2/pet', headers={'accept': 'application/json','Content-Type': 'application/json'}, data=json.dumps(body))

print(res)
print(res.json())
print(type(res.json()))

res_json = json.loads(res.text)
assert body == res_json

#PUT Update an existing pet

body = {"id": 10,
        "category": {"id": 10, "name": "Alex"},
        "name": "dog",
        "photoUrls": ['string'],
        "tags": [{"id": 11, "name": "Dog1"}],
        "status": "available"}

res = requests.put(url=f'https://petstore.swagger.io/v2/pet', headers={'accept': 'application/json','Content-Type': 'application/json'}, data=json.dumps(body))

print(res)
print(res.json())
print(type(res.json()))


#DELETE Deletes a pet

res = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{body["id"]}')

print(res)
print(res.json())
