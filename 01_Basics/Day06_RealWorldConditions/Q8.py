# Simple username/password login check.
# Test cases:
# Input: admin,python123
# Expected output: Login successful
# Input: admin,wrong
# Expected output: Invalid credentials

uname=input("Enter your user name: ")
password=input("Enter your password: ")
if uname=='admin' and password=='python123':
    print("login successful")
else:
    print("invalid credentiatls")