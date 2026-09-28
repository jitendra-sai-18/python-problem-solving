# Write a program that accepts a journey's distance in kilometres and duration in hours. Calculate the average speed in kilometres per hour.
# Required inputs: Distance and duration (floats)
# Display the average speed. Assume the duration is greater than zero.

dist=float(input("Enter the distance :"))
hrs=float(input("Enter the hours :"))
avg=dist/hrs
print("The average speed is ",avg)