# Find the incorrect assumptions
x = 5
y = "5"
z = 5.0

x = y
y = z
z = x

print(type(x))
print(type(y))
print(type(z))