import json
import requests

url = 'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&artist=Cher&album=Believe&format=json'

data = requests.get(url).text
print type(data)
print(data)
