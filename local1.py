import requests

BASE = "http://127.0.0.1:5000/"

data = [{"firstName": "Dmitry", "lastName": "Vyatskin", "email": "trackinghell@.gmail.com", "password": "012345"},
        {"firstName": "Sonya", "lastName": "Sergeeva", "email": "sonya451f@gmail.com", "password": "0166645"},
        {"firstName": "Mark", "lastName": "Gorbenko", "email": "vpopydal@gmail.com", "password": "346758"}]


# for i in range(len(data)+1):
#     response = requests.delete(BASE + "api/accounts/" + str(i+1))
#     print(response)


for i in range(len(data)):
    response = requests.put(BASE + "api/accounts/" + str(i+1), json=data[i])
    print(response.json())

response = requests.get(BASE + "api/accounts/1")
if response.status_code == 200:
    print(response.json())
else:
    print("Error: response status code is...")


# input()
# response = requests.delete(BASE + "api/accounts/2")
# print(response)

# print(response.json()) #выводим наш запрос в формате json