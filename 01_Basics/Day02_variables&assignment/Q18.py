# Swap two variables without losing their values
# a = 100
# b = 200
# Write a program that swaps the values of a and b.
# Requirements:
# - Do not simply assign a = 200 and b = 100.
# - Use a temporary variable to help perform the swap.
# - Print a and b on separate lines after swapping.
a=100
b=200
temp=a
a=b
b=temp
print(a)
print(b)