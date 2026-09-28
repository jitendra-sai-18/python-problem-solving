# Write a program that accepts the price of one notebook, the price of one pen, and the quantities purchased. Calculate the cost of each item category and the combined cost.
# Required inputs: Prices (floats), quantities (integers)
# Display both subtotals and the grand total.

penprice=float(input("Enter the penprice:"))
book=float(input("Enter the book price:"))
penqnt=int(input("Enter the quantity of pen:"))
bookqnt=int(input("Enter the quantity of book:"))
pensprice=penprice*penqnt
bookprice=book*bookqnt
totalprice=pensprice+bookprice
print("The total price is ",totalprice)
print("The pens price is ",pensprice)
print("The books price is ",bookprice)