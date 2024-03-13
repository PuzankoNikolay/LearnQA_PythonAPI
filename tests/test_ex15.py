from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from random import choice
from string import ascii_letters
import pytest
import allure

class TestUserRegister(BaseCase):
    params = [
        ('password'),
        ('username'),
        ('firstName'),
        ('lastName'),
        ('email')
    ]

    def test_create_user_with_invalid_email(self):
        email = 'vvinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", \
            f"Unexpected content {response.content}"

    @pytest.mark.parametrize('condition', params)
    @allure.title("Test Authentication (condition: {condition})")
    def test_create_user_with_null(self, condition):
        data = self.prepare_registration_data()
        data.update({condition: ''})
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of '{condition}' field is too short", \
            f"Unexpected content {response.content}"

    def test_create_user_with_short_name(self):
        username = (''.join(choice(ascii_letters) for i in range(1)))
        data = self.prepare_ex15_data(username)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short", \
            f"Unexpected content {response.content}"

    def test_create_user_with_long_name(self):
        username = (''.join(choice(ascii_letters) for i in range(251)))
        data = self.prepare_ex15_data(username)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long", \
            f"Unexpected content {response.content}"
