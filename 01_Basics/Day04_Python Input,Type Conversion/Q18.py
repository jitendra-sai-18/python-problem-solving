# Write a program that accepts a student's name and marks in five subjects, each out of 100. Calculate the total, average, and overall percentage.
# Required inputs: Name (string), five marks (numbers)
# Display the student's name, total out of 500, average, and percentage. Do not use conditions to assign grades.

std=input("enter student name:")
sub1=int(input("enter subject 1:"))
sub2=int(input("enter subject 2:"))
sub3=int(input("enter subject 3:"))
sub4=int(input("enter subject 4:"))
sub5=int(input("enter subject 5:"))
total=sub1+sub2+sub3+sub4+sub5
avg=total/5
per=total/500*100
print("name:",std)
print("total marks out of 500 is:",total)
print("average marks out of 100 is:",avg)
print("percentage is:",per)