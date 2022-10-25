'''5. Write a program to find the greatest number from the three numbers'''
n1=int(input("enter n1: ")) 
n2=int(input("enter n2: "))
n3=int(input("enter n3: ")) 

if (n1>n2 and n1>n3):
  print("{} is greater".format(n1))
elif(n2>n1 and n2>n3):
  print("{} is greater".format(n2))
else:
  print("{} is greater".format(n3))
