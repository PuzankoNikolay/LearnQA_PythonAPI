from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

class TestUserDelete(BaseCase):

    def test_delete_2(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        with allure.step("LOGIN"):
            response1 = MyRequests.post("/user/login", data=data)

            auth_sid = self.get_cookie(response1, "auth_sid")
            token = self.get_header(response1, "x-csrf-token")

        with allure.step("DELETE"):
            response2 = MyRequests.delete(
                f"/user/2",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
                data=data
            )
            Assertions.assert_code_status(response2, 400)


    def test_delete_created_user_by_himself(self):
        with allure.step("REGISTER"):
            register_data = self.prepare_registration_data()
            response1 = MyRequests.post("/user/", data=register_data)

            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")

            email = register_data['email']
            password = register_data['password']
            user_id = self.get_json_value(response1, "id")

        with allure.step("LOGIN"):
            login_data = {
                'email': email,
                'password': password
            }
            response2 = MyRequests.post("/user/login", data=login_data)

            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step("DELETE"):
            response3 = MyRequests.delete(
                f"/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
                data=login_data
            )

            Assertions.assert_code_status(response3, 200)


        with allure.step("GET"):
            response4 = MyRequests.get(f"/user/{user_id}")
            assert response4.content.decode("utf-8") == f"User not found", \
                f"Unexpected content {response4.content}"

    @allure.issue("someurl.ru", name="known_bug")
    def test_delete_user_by_another(self):
        with allure.step("REGISTER"):
            register_data = self.prepare_registration_data()
            response1 = MyRequests.post("/user/", data=register_data)

            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")

            email = register_data['email']
            username = register_data['username']
            password = register_data['password']
            user_id = self.get_json_value(response1, "id")

        with allure.step("LOGIN"):
            login_data = {
                'email': email,
                'password': password
            }
            response2 = MyRequests.post("/user/login", data=login_data)

            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step("DELETE"):
            response3 = MyRequests.delete(
                f"/user/94636",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
                data=login_data
            )

            Assertions.assert_code_status(response3, 200)

        with allure.step("GET DELETED"):
            response4 = MyRequests.get(f"/user/94636")
            Assertions.assert_code_status(response4, 200)

        with allure.step("GET CREATED (bugged)"):
            response5 = MyRequests.get(f"/user/{user_id}")
            print(response5.text)
            Assertions.assert_code_status(response5, 200)
