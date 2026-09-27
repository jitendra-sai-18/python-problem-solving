# Predict the value and data type of every variable at the end of the program.
a = 10
b = 10.0
c = "10"
d = True

a = c
c = b
b = d
d = a
a = 25

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))