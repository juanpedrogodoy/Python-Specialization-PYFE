# Project: Hourly Email Distribution Tracker
# Course: PY4E - Module 2 (Tuples)
# Description: This script analyzes the distribution of emails by hour of the day.
# It uses a dictionary for counting and tuples to sort the final results by hour.
# ---------------------------------------------------------------------------

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for lines in handle:
    if not lines.startswith("From "):
        continue
    line = lines.split()
    
    # Extracting the time string (index 5) and then the hour (first 2 chars)
    hours = line[5]
    hour = hours[:2]
    counts[hour] = counts.get(hour, 0) + 1

# Using a list of tuples to sort by the key (hour)
lst = list()
for key, value in counts.items():
    newtup = (key, value)
    lst.append(newtup)

# Sorting the list of tuples alphabetically/numerically by the first element
lst = sorted(lst)

for key, value in lst:
    print(key, value)
