# Write a program that accepts three integers and calculates their sum, product, and average.
# Required inputs: Three integers
# Display the sum, product, and average. Ensure the average can contain a decimal.
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
sum=num1+num2+num3
product=num1*num2*num3
avg=sum/3
print("the sum is",sum)
print("the product is",product)
print("the average is",avg)