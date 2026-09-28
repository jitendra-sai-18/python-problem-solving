# Write a program that accepts a monthly basic salary. Calculate the house rent allowance (20% of basic salary), travel allowance (8% of basic salary), gross monthly salary, and annual gross salary.
# Required inputs: Basic monthly salary (float)
# Display both allowances, gross monthly salary, and annual gross salary.

basicsal=float(input("Enter the basic salary :"))
hra=basicsal*20/100
tra=basicsal*8/100
grossmonth=basicsal+hra+tra
grossyear=grossmonth*12
print("house rent allowens is:",hra)
print("travel allowens is:",tra)
print("grossmontly salary is:",grossmonth)
print("grossyear is:",grossyear)