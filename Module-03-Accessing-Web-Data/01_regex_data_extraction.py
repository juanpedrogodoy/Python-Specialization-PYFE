# Project: Regular Expression Data Extractor
# Course: PY4E - Module 3 (Regular Expressions)
# Description: This script reads a file and uses the 're' library to find 
# all sequences of numbers within the text, converting them to integers 
# and calculating their total sum.

import re 

total = 0 
nam = input("Enter file: ") 
if len(nam) < 1: 
    nam = "mbox-short.txt" 

try: 
    handle = open(nam) 
except: 
    print("File does not exist") 
    quit() 

for lines in handle: 
    lines = lines.rstrip()
    # findall returns a list of all strings that match the pattern [0-9]+
    y = re.findall('[0-9]+', lines) 
    for numbers in y: 
        n = int(numbers) 
        total = total + n 

print("The total sum is:", total)
