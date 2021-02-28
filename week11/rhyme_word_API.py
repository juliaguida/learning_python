import requests

parameter = {"rel_rhy":"peace"}
request = requests.get('https://api.datamuse.com/words',parameter)
response = request.json()
print(request.status_code)
for word in response[0:3]:
    print(word)
