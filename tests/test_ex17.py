from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from random import choice
from string import ascii_letters
import allure

class TestEx17(BaseCase):
    def test_negative_edit(self):
        with allure.step("UNAUTHORIZED EDIT"):
            new_name = "Changed name"
            response1 = MyRequests.put(
                f"/user/94637",
                data={"firstName": new_name}
            )
            Assertions.assert_code_status(response1, 400)

        with allure.step('LOGIN'):
            login_data = {
                'email': 'learnqa03132024111720@example.com',
                'password': '123'
            }
            response2 = MyRequests.post("/user/login", data=login_data)

            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")
            user_id_from_auth_method = self.get_json_value(response2, "user_id")

        with allure.step('INVALID EMAIL EDIT'):
            email = (''.join(choice(ascii_letters) for i in range(10)) + '.com')
            response4 = MyRequests.put(
                f"/user/{user_id_from_auth_method}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
                data={"email": email}
            )
            Assertions.assert_code_status(response4, 400)

        with allure.step('SHORT FIRSTNAME EDIT'):
            new_name = (''.join(choice(ascii_letters) for i in range(1)))
            response5 = MyRequests.put(
                f"/user/{user_id_from_auth_method}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
                data={"firstName": new_name}
            )
            Assertions.assert_code_status(response5, 400)

    @allure.issue("someurl.ru", name="known_bug")
    def test_negative_edit_bug(self):
        with allure.step('LOGIN'):
            login_data = {
                'email': 'learnqa03132024111720@example.com',
                'password': '123'
            }
            response2 = MyRequests.post("/user/login", data=login_data)

            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step('INVALID AUTHORIZATION EDIT'):
            new_name = "Changed name"

            response3 = MyRequests.put(
                f"/user/94637",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
                data={"firstName": new_name}
            )
            Assertions.assert_code_status(response3, 400)
            