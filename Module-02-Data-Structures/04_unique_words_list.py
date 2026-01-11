# Unique Word Organizer
# PY4E - Module 2 (Lists)
# This script reads a file (like romeo.txt), breaks it into individual words, and builds a sorted list containing only unique words (no duplicates).

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File not found")
    quit()

lst = list()
for line in fh:
    # Splitting the line into a list of words
    words = line.split()
    for word in words:
        # Checking for duplicates before adding
        if not word in lst:
            lst.append(word)
            # Sorting the list to keep it organized
            lst.sort()

print(lst)
