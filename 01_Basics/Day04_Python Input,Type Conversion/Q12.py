# Write a program that accepts a total number of minutes as an integer and converts it into total seconds and total hours.
# Required inputs: Minutes (integer)
# Display seconds and hours. Hours may be decimal.
minutes=int(input("Enter the number of minutes :"))
sec=minutes*60
hrs=minutes/60
print("the number of hours :",hrs)
print("the number of seconds :",sec)