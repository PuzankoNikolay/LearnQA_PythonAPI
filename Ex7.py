import requests
method = ['GET', 'POST', 'PUT', 'DELETE']
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
for i in range(len(method)):
    response = requests.request(method[i], url)
    print("1.", response.text)

# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response = requests.head(url)
print("2.", response.text)

# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
for i in range(len(method)):
    if method[i] == 'GET':
        params = {'method': method[i]}
        response = requests.request(method[i], url, params=params)
        print("3.", response.text)
    else:
        params = {'method': method[i]}
        response = requests.request(method[i], url, data=params)
        print("3.", response.text)

# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
for i in range(len(method)):
    if method[i] == 'GET':
        for k in range(len(method)):
            params = {'method': method[k]}
            response = requests.request(method[k], url, params=params)
            print("4.", method[i], params, response.text)
    else:
        for k in range(len(method)):
            params = {'method': method[k]}
            response = requests.request(method[i], url, data=params)
            print("4.", method[i], params, response.text)