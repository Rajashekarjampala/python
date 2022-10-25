''' 1. Write a program to find larger of two numbers.'''

n1=int(input("enter : n1 ")) 
n2=int(input("enter : n2 "))

if (n1>n2):
  print("{} is greater".format(n1))
elif(n1==n2):
  print("{a} is equal to {b}".format(b=n1,a=n2))
else:
  print("{} is greater".format(n2))