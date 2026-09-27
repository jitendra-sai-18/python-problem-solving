# Predict the exact output.
a = 7
b = "7"
c = 7.0
a = b
b = a
c = b
a = 7.0
b = True
c = a
print(a, type(a))
print(b, type(b))
print(c, type(c))