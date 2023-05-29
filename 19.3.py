import requests

'''Запрос get'''

status = "available"

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={"accept":"application/json"})

print(res.status_code)
print(res.text)
print(type(res.json()))

"""Запрос Post"""

url = 'https://petstore.swagger.io/v2/user'

headers = {
     'accept': 'application/json',
     'Content-Type': 'application/json'
}

data = {
     "id": 0,
     "username": "Test5",
     "firstName": "test",
     "lastName": "test",
     "email": "test",
     "password": "test",
     "phone": "test",
     "userStatus": 0
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

"""Запрос Put"""

url = 'https://petstore.swagger.io/v2/user/Test5'

headers = {
     'accept': 'application/json',
     'Content-Type': 'application/json'
}

data = {
     "id": 0,
     "username": "Test6",
     "firstName": "test",
     "lastName": "test",
     "email": "test",
     "password": "test",
     "phone": "test",
     "userStatus": 0
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())


'''Запрос Delete'''

url = 'https://petstore.swagger.io/v2/user/Test6'

headers = {
    'accept': 'application/json'
}

response = requests.delete(url, headers=headers)

print(response.status_code)
print(response.json())
