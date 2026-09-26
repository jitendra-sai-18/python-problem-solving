# Carefully predict the output of this program:
# a = 10
# b = 20
# c = 30
#
# a = b
# b = c
# c = a
#
# a = a + 5
# b = b - a
# c = c + b
#
# print(a)
# print(b)
# print(c)
# Trace all three variables from the first line to the last.
#  Remember that assigning one variable to another copies its current value.
#  Remember that changing one variable does not automatically change the others.
#  Write the exact output, followed by a short explanation of your reasoning.
a = 10
b = 20
c = 30

a = b
b = c
c = a

a = a + 5
b = b - a
c = c + b

print(a)
print(b)
print(c)
