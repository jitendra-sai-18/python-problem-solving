# Calculate total, average and pass/fail for three marks; all must be >=35.
# Test cases:
# Input: 80 70 60
# Expected output: Total:210, Average:70.0, Pass
# Input: 80 30 70
# Expected output: Total:180, Average:60.0, Fail
sub1=int(input("Enter a subject 1 marks: "))
sub2=int(input("Enter a subject 2 marks: "))
sub3=int(input("Enter a subject 3 marks: "))
total=sub1+sub2+sub3
print("Total:",total)
average=total/3
print("Average:",average)
if sub1>=35 and sub2>=35 and sub3>=35:
    print("pass")
else:
    print("fail")