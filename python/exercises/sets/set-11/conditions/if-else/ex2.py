'''Write a program to read two numbers. Then find out whether the first number is a multiple of the
second number.'''

n1=int(input("Enter number n1: "))
n2=int(input("Enter number n2: "))

if(n1%n2==0):
  print("n1 is multiple of n2: ")
else:
  print("n1 is not multiple of n2: ")