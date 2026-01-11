# Overtime Pay Calculator
# PY4E - Module 1
# My first implementation of if/else.
# It calculates total pay including a 1.5x bonus for extra hours.

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

if fh > 40:
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    payment = reg + otp
else:
    payment = fh * fr

print("Pay:", payment)
