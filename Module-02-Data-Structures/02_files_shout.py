# Project: File Reader - Shouting Mode
# Course: PY4E - Module 2 (Files)
# Description: This script opens a file, reads it line by line, 
# removes extra whitespace, and prints everything in uppercase.

# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be opened: ", fname)
    quit()

for x in fh:
    x = x.rstrip()
    x = x.upper()
    print(x)
