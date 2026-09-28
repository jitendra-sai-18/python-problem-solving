# Write a program that accepts marks for four subjects. Calculate the total marks and average marks. Assume each subject is out of 100.
# Required inputs: Four subject marks (numbers)
# Display the total out of 400 and the average out of 100.
sub1=int(input("enter the sub1 marks out of 100:"))
sub2=int(input("enter the sub2 marks out of 100:"))
sub3=int(input("enter the sub3 marks out of 100:"))
sub4=int(input("enter the sub4 marks out of 100:"))
total=sub1+sub2+sub3+sub4
avg=total/4

print("the total marks is",total)
print("the average marks is",avg)