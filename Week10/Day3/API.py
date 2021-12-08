# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 18:15:26 2021

@author: 97250
"""

import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
# Print the status code of the response.
print(response.status_code)
# 200 

print(response.json())


parameters = {"lat": 31.771959, "lon": 35.217018}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(response.text)

response = requests.get("http://api.open-notify.org/astros.json")
data = response.text
print(response.request.url)
print(response.request.body)
# http://api.open-notify.org/astros.json                                   
# None   

response = requests.get("http://api.open-notify.org/astros.json")

# Print the content of the response (the data the server returned)
data = response.json()

print(data)