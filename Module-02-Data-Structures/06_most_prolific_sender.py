# Project: Email Frequency Counter (Dictionaries)
# Course: PY4E - Module 2 (Dictionaries)
# Description: This script identifies the person who sent the most emails.
# It uses a dictionary to create a frequency histogram and then 
# iterates through it to find the maximum value.

counts = dict()
nam = input("Enter file: ")

# Shortcut to use the default file if just Enter is pressed
if len(nam) < 1:
    nam = "mbox-short.txt"

try:
    handle = open(nam)
except:
    print("File does not exist")
    quit()

for lines in handle:
    if not lines.startswith("From "):
        continue
    line = lines.split()
    emails = line[1]
    # The 'get' method handles cases where the email is not yet in the dict
    counts[emails] = counts.get(emails, 0) + 1

# Finding the most frequent sender
bigword = None
bigcount = None
for emails, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = emails
        bigcount = count

print(bigword, bigcount)
