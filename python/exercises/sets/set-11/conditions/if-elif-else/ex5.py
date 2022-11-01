'''7. Write a program to calculate tax given the following conditions:
If income is less than 1,50,000 then no tax
If taxable income is 1,50,001 - 3,00,000 then charge 10% tax
If taxable income is 3,00,001 - 5,00,000 then charge 20% tax
If taxable income is above 5,00,001 then charge 30% tax'''

def check_tax(income):

  if (income<150000):
    return("No Tax")

  elif(income>150001 and income<=300000):
    return("tax: ",income*(10/100))

  elif(income>300001 and income<500000):
    return("tax: ",income*(20/100))

  elif(income>500001):   
    return("tax: ",income*(30/100)) 

print(check_tax(4000000))    