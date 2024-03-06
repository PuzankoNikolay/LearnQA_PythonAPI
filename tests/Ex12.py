import requests
class TestEx12:
    def test_cookie_method(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        headers = response.headers
        print(headers)
        print((headers['x-secret-homework-header']))
        a = headers['x-secret-homework-header']
        b = 'Some secret value'
        assert a == b, f"Значением секретного заголовка является '{a}'"