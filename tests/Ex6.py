import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
last_response = response
print("Количество редиректов:", len(response.history))
print("Конечный URL:", last_response.url)