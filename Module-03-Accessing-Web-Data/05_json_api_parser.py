# JSON Data Processor
# PY4E - Module 3 (Web Data)
# This script retrieves JSON data from an API, parses the string into a Python dictionary, and iterates through nested lists to sum numerical values.

import urllib.request
import json

counter = 0
total = 0
url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2337839.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# info becomes a dictionary representing the JSON object
info = json.loads(data)

# 'comments' is a list of dictionaries inside the main dictionary
comments = info["comments"]

for items in comments:
    counter = counter + 1
    # Accessing the 'count' value for each user/comment
    total = total + items["count"]

print("Count:", counter)
print("Sum:", total)
