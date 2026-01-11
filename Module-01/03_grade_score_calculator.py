# Grade Score Calculator
# PY4E - Module 1
# This script converts a numerical score (0.0 - 1.0) 
# into a letter grade using if/elif/else.

score = input("Enter Score: ")
score = float(score)
if score > 1.0:
    print ("Out of range")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score <0.6:
    print("F")
elif score <0.0:
    print("Out of range")
