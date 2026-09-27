# The final boss: Trace, predict, and debug
# This program contains several reassignment steps.
# a = 20
# b = "20"
# c = 20.0
# d = False
#
# a = b
# c = a
# b = d
# d = c
# a = 20.5
# c = b
# b = a
#
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))
# Task A — Trace: Determine the final value and data type of each variable.
# Task B — Predict: Write the exact four lines of output.
# Task C — Debug your reasoning: A student says, "When a changes, every variable that previously received the value of a changes too."
# Explain why this reasoning is incorrect, using at least one specific assignment from the program.


a = 20
b = "20"
c = 20.0
d = False

a = b
c = a
b = d
d = c
a = 20.5
c = b
b = a

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))