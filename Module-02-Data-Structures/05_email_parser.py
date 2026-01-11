# Project: Email Address Extractor
# Course: PY4E - Module 2 (Lists & Files)
# Description: This script scans an email log file to find lines 
# starting with 'From '. It then splits those lines to extract 
# and print the sender's email address and counts the total.

# Please use mbox-short.txt
fname = input("Enter file name: ")
count = 0

try:
    fh = open(fname)
except:
    print("File not found")
    quit()

for line in fh:
    if line.startswith("From "):
        # split() creates a list of words from the line
        words = line.split()
        count = count + 1
        # words[1] is the second element (the email address)
        print(words[1])

print("There were", count, "lines in the file with From as the first word")
