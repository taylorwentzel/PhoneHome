import requests
payload = {'name':'Taylor Wentzel', 'username': 'taylorwentzel'}
r = requests.post('https://ghatracker.herokuapp.com/', json=payload)