# Overtime Pay Calculator using Functions
# PY4E - Module 1
# Refactoring the pay calculator logic into a reusable function called 'computepay'.
# This demonstrates parameter passing and returning values.

def computepay(h, r):
    if h > 40:
        reg= h * r
        otp= (h - 40) * (r * 0.5)
        payment= reg + otp
    else : payment = h * r
    return payment

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay", p)
