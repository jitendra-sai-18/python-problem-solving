# Write a program that estimates the cost of a small event. Accept the number of guests, food cost per guest, venue rent, and decoration cost. Calculate the food cost, total event budget, and cost per guest.
# Required inputs: Guests (integer); costs (floats)
# Display food cost, total budget, and cost per guest. Assume the number of guests is greater than zero.

g=int(input("enter the number of guests:"))
c=float(input("enter the food cost per guest:"))
v=float(input("enter the venue rent:"))
d=float(input("enter the decoration coast:"))
fc=g*c
totalbudget=fc+v+d
cpg=totalbudget/g
print("food cost is:",fc)
print("the total budget is:",totalbudget)
print("cost per guest is:",cpg)