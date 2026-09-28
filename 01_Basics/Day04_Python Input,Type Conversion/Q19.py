# Write a program that accepts a rectangular tank's length, width, and water height in metres. Calculate the water volume in cubic metres and convert it to litres. Use 1 cubic metre = 1000 litres.
# Required inputs: Length, width, water height (floats)
# Display the volume in cubic metres and litres.

l=float(input("enter length of tank:"))
w=float(input("enter width of tank:"))
h=float(input("enter water height in tank:"))
v=l*w*h
ltr=v*1000
print("the vol in cubic meters is:",v)
print("the water in tank in liters  is:",ltr)






