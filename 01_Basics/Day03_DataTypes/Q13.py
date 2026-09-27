# Predict the exact output.
x = 25
y = "25"
z = 25.0

print(type(x))
print(type(y))
print(type(z))

x = y
y = "25.0"
z = x

print(type(x))
print(type(y))
print(type(z))