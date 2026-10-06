# Shopping discount: >=5000 20%, >=2000 10%, otherwise 0%.
# Test cases:
# Input: 6000
# Expected output: 4800.0
# Input: 2500
# Expected output: 2250.0
amount=int(input("enter the bill amount:"))
if amount>=5000:
    discount=amount*(20/100)
    total_amt=amount-discount
    print(total_amt)
elif amount>=2000:
    discount=amount*0.10
    total_amt=amount-discount
    print(total_amt)
else:
    print(amount)