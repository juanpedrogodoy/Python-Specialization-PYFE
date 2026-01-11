# Email Data Extractor (Spam Confidence)
# PY4E - Module 2 (Files & Strings)
# This script parses an email log file, filters specific lines, 
# extracts numerical data, and calculates the statistical average.
# It demonstrates data filtering using 'continue'.

# Use the file name mbox-short.txt as the file name
count = 0
add = 0
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("File not found: ", fname)
    quit()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    # Logic for lines that match the criteria
    count = count + 1
    ini = line.find("0")
    num = line[ini:]
    fnum = float(num)
    add = add + fnum

average = add / count
print("Average spam confidence:", average)
print("Done")
