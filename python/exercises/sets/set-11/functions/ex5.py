'''
    Write a function to calculate the employes's  Income ,based on Income.
   There are 5 different taxes to the employees.
   You need to find the Income of the employee and Print there taxes.
   Here's the table to calculcate the taxes
   Note: 
       1. You must use **kwargs       
       2. If the input income is non-integer, you must raise exception since income can be in integers ONLY

   ----------------------------
       INCOME                 TAX
       ------                ------
        >500000                30%
        300000-500000          20%
        100000-300000          10%
        50000-100000           5%
        <50000                 1%        
'''
def check_tax(**income_emp):
  for name,income in income_emp.items():
    if (type(income)==str):
      return ("Income can be in integers ONLY")

  if (income>500000):
    return('{} income tax is {}'.format(name,income*30/100))  
  elif (income>=300000 and income<500000):
    return ('{} income tax is {}'.format(name,income*20/100))
  elif (income>=100000 and income<300000):
    return ('{} income tax is {}'.format(name,income*10/100)) 
  elif (income>=50000 and income<100000):
    return ('{} income tax is {}'.format(income*5/100))  
  elif (income<50000):
    return ('{} income tax is {}'.format(name,income*1/100))  

print(check_tax(Raj=120000,Sai=300000))    
  
  
