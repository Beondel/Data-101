import json
import requests

url = "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=dd3dfa53791e926be558bad1086a8fa1&artist=Cher&album=Believe&format=json"

data = requests.get(url).text
print type(data)
print(data)
