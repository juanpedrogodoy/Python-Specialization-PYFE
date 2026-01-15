# Project: Web Scraping with BeautifulSoup
# Course: PY4E - Module 3 (Web Data)
# Description: This script scrapes a webpage to find all <span> tags,
# extracts the numerical data within them, and calculates the total sum.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors (crucial for modern https websites)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# Reading the entire HTML content
html = urlopen(url, context=ctx).read()
# Parsing the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

count = 0
total = 0

# Retrieve all 'span' tags from the parsed HTML
tags = soup.find_all('span')
for tag in tags:
    # Access the content inside the span tag
    number = tag.contents[0]
    num = int(number)
    count = count + 1
    total = total + num

print("Count:", count)
print("Sum:", total)
