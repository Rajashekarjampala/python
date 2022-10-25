'''3. Write a program using for loop to print all the numbers from n1-n2 thereby classifying them as even or
odd.'''

n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))

for i in range(n1,n2):
  if (i%2==0):
    print(i,'is Even number')

  else:
    print(i,'is Odd number')