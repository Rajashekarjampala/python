'''8. Write a program to enter the marks of a student in four subjects. Then calculate the total and aggregate,
and display the grade obtained by the student. If the student scores an aggregate greater than 75%, then
the grade is Distinction. If aggregate is 60>= and <75, then the grade is First Division. If aggregate is 50>=
and <60, then the grade is Second Division. If aggregate is 40>= and <50, then the grade is Third Division.
Else the grade is fail.'''

s1=int(input("enter marks s1: "))
s2=int(input("enter marks s2: "))
s3=int(input("enter marks s3: "))
s4=int(input("enter marks s4: "))

avg=(s1+s2+s3+s4)/4
print("avarage: ",avg)

if (avg>=75 and avg<=100):
  print("distinction")
elif(avg>=60 and avg<75):
  print("first division")
elif(avg>=50 and avg<60):
  print("second division")
elif(avg>=40 and avg<50):
  print("Failed")
else:
  print("failed")