import requests
payload = {'name':'Taylor', 'username': 'taylorwentzel'}
r = requests.post('https://ghatracker.herokuapp.com/about', json=payload)