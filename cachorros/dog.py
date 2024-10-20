import requests
import pandas as pd

url = 'https://http.dog/101.jpg'
req = requests.get(url, timeout=3)
dog = req.json()
print(dog)