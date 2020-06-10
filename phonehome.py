import requests
payload = {'name':'Taylor', 'username': 'taylorwentzel'}
r = requests.post('localhost:5000', json=payload)