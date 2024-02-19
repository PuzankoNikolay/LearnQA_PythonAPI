import requests
import json
import time
url = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.request('GET', url)
key = "token"
obj = json.loads(response.text)
if key in obj:
    params = {"token":obj[key]}
    response = requests.request('GET', url, params=params)
    poisk_statusa = json.loads(response.text)
    stat = "status"
    if poisk_statusa[stat] == "Job is NOT ready":
        print("Job is NOT ready")
    else:
        print("Status in not OK")
sec = "seconds"
if sec in obj:
    t = int(obj[sec])
    time.sleep(t)
response = requests.request('GET', url, params=params)
poisk_result = json.loads(response.text)
res = "result"
if poisk_result[stat] == "Job is ready" and res in poisk_result:
    print("Job is ready. It took", poisk_result[res], 'seconds')
else:
    print("Status or result in not OK")