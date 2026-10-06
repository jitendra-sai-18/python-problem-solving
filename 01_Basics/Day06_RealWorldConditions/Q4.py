# Electricity bill: first 100 units ₹2, next 100 ₹3, above 200 ₹5.
# Test cases:
# Input: 50
# Expected output: 100
# Input: 150
# Expected output: 350
# Input: 250
# Expected output: 850
unit=int(input("Enter a number of units: "))
if unit<=100:
    funit=unit*2
    print(funit)
elif unit<=200:
    sunit=unit-100
    funit=200+(sunit*3)
    print(funit)
else:
    sunit=unit-200
    funit=200+300+(sunit*5)
    print(funit)
