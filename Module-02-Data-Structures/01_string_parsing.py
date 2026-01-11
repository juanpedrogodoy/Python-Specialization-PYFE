# String Parsing
# PY4E - Module 2 (Strings)
# This is my original solution. It works by finding the specific 
# character '0' to start the slicing.

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find("0")
host = text[pos:]
fhost = float(host)
print(fhost)
