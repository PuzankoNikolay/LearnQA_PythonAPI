import requests
class TestEx11:
    def test_cookie_method(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        cookies = response.cookies
        for cookie in cookies:
            cookie_name = cookie.name
            cookie_value = cookie.value
            print(f"Cookie name: {cookie_name}, value: {cookie_value}")
        assert cookie_name == "HomeWork", f"Именем куки является {cookie_name}"
        assert cookie_value == "hw_value", f"Значением куки является {cookie_value}"