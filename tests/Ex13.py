import requests
import pytest
class TestEx13:
    params = [
        ('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'),
        ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'),
        ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'),
        ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'),
        ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
    ]
    @pytest.mark.parametrize('condition', params)
    def test_user_agent(self, condition):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        response = requests.get(url, headers={"User-Agent":condition})
        user_agent = response.json()
        if user_agent['user_agent'] == 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30':
            assert user_agent['platform'] == 'Mobile',f"'platform' is not 'Mobile', it is '{user_agent['platform']}'!"
            assert user_agent['browser'] == 'No',f"'browser' is not 'No', it is '{user_agent['browser']}'!"
            assert user_agent['device'] == 'Android',f"'device' is not 'Android', it is '{user_agent['device']}'!"
        elif user_agent['user_agent'] == 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1':
            assert user_agent['platform'] == 'Mobile', f"'platform' is not 'Mobile', it is '{user_agent['platform']}'!"
            assert user_agent['browser'] == 'Chrome', f"'browser' is not 'Chrome', it is '{user_agent['browser']}'!"
            assert user_agent['device'] == 'iOS', f"'device' is not 'iOS', it is '{user_agent['device']}'!"
        elif user_agent['user_agent'] == 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)':
            assert user_agent['platform'] == 'Googlebot', f"'platform' is not 'Googlebot', it is '{user_agent['platform']}'!"
            assert user_agent['browser'] == 'Unknown', f"'browser' is not 'Unknown', it is '{user_agent['browser']}'!"
            assert user_agent['device'] == 'Unknown', f"'device' is not 'Unknown', it is '{user_agent['device']}'!"
        elif user_agent['user_agent'] == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0':
            assert user_agent['platform'] == 'Web', f"'platform' is not 'Web', it is '{user_agent['platform']}'!"
            assert user_agent['browser'] == 'Chrome', f"'browser' is not 'Chrome', it is '{user_agent['browser']}'!"
            assert user_agent['device'] == 'No', f"'device' is not 'No', it is '{user_agent['device']}'!"
        elif user_agent['user_agent'] == 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1':
            assert user_agent['platform'] == 'Mobile', f"'platform' is not 'Mobile', it is '{user_agent['platform']}'!"
            assert user_agent['browser'] == 'No', f"'browser' is not 'No', it is '{user_agent['browser']}'!"
            assert user_agent['device'] == 'iPhone', f"'device' is not 'iPhone', it is '{user_agent['device']}'!"

