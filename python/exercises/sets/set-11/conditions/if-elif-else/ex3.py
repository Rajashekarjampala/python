'''5. Write a program to find the greatest number from the three numbers'''

def check_num(num1,num2,num3):

  if (num1>num2 and num1>num3):
    return("{} is greater".format(num1))
  elif(num2>num1 and num2>num3):
    return("{} is greater".format(num2))
  else:
    return("{} is greater".format(num3))

print(check_num(10,20,30))