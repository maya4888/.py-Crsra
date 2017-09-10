# This first line is provided for you
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h>40:
    pay = h*r
    xp = float((h-40)*(r*0.5))
grossPay = pay + xp
print(grossPay)
