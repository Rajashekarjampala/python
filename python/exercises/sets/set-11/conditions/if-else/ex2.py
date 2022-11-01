'''Write a program to read two numbers. Then find out whether the first number is a multiple of the
second number'''

def check_num(num1,num2):
  if(num1%num2==0):
    return("n1 is multiple of n2: ")
  else:
    return("n1 is not multiple of n2: ")

print(check_num(20,5))    