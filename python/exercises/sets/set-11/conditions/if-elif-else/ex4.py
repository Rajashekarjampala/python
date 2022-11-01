''' 1. Write a program to find larger of two numbers.'''

def check_num(num1,num2):
  if (num1>num2):
    return("{} is greater".format(num1))
  elif(num1==num2):
    return("{a} is equal to {b}".format(b=num1,a=num2))
  else:
    return("{} is greater".format(num2))

print(check_num(100,200))