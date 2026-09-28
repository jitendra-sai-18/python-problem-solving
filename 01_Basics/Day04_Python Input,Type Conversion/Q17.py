# Write a program that accepts the total journey distance in kilometres, the vehicle's average mileage in kilometres per litre, and the fuel price per litre. Calculate the fuel required and estimated fuel cost.
# Required inputs: Distance, mileage, and fuel price (floats)
# Display the required litres of fuel and the estimated cost. Assume mileage is greater than zero.

dist=int(input("enter the distance of journey:"))
m=int(input("enter the mileage:"))
fp=float(input("enter the fuel price:"))
fr=dist/m
fc=fr*fp
print("fuel required:",fr)
print("total fuel cost is:",fc)

