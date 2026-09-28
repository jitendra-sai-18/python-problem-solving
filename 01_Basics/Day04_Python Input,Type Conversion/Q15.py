# Write a program for a purchase of three products. Accept each product's price and quantity. Calculate the subtotal, a 10% discount, and the final bill after the discount.
# Required inputs: Three prices (floats), three quantities (integers)
# Display each product's cost, subtotal, discount amount, and final bill. Apply the discount to the subtotal

product1=float(input("Enter the price of the product1 :"))
prdqnt1=int(input("Enter the quantity of the product1 :"))
product2=float(input("Enter the price of the product2 :"))
prdqnt2=int(input("Enter the quantity of the product2 :"))
product3=float(input("Enter the price of the product3 :"))
prdqnt3=int(input("Enter the quantity of the product3 :"))
totalp1=product1*prdqnt1
totalp2=product2*prdqnt2
totalp3=product3*prdqnt3
subtotal=totalp1+totalp2+totalp3
discount=subtotal*0.1
finalprice=subtotal-discount
print("product1 price is ",product1)
print("product1 total price is",totalp1)
print("product2 price is ",product2)
print("product2 total price is",totalp2)
print("product3 price is ",product3)
print("product3 total price is",totalp3)
print("total cost is",subtotal)
print("total discount amount is",discount)
print("final price is ",finalprice)

