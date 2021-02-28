import requests

request = requests.get('http://api.open-notify.org/astros.json')
print(request.text)
#print(request.status_code)
request = request.json()
people_in_space = request['people']
print('The number of people in space today is',len(people_in_space))
for people in people_in_space:
    print(people['name'])

