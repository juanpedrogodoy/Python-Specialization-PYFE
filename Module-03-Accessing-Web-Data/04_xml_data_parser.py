# XML Data Extractor
# PY4E - Module 3 (Web Data)
# This script retrieves XML data from a URL, parses the
# tree structure using ElementTree, and sums all 'count' values.

import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2337838.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# Parse the XML string into an element tree
tree = ET.fromstring(data)

# Use XPath to find all 'count' elements anywhere in the tree
counts = tree.findall('.//count')
nums = list()

for result in counts:
    # Extract text from the element and convert to integer
    number = int(result.text)
    nums.append(number)

print('Count:', len(nums))
print('Sum:', sum(nums))
