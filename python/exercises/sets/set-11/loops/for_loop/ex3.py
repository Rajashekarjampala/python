'''3. Write a program using for loop to print all the numbers from n1-n2 thereby classifying them as even or
odd.'''

even_list=[]
odd_list=[]
def check_num(num1,num2):

  for i in range(num1,num2):
    if (i%2==0):
      even_list.append(i)
    else:
      odd_list.append(i)

  return ("{} is Even list\n{} is odd list".format(even_list,odd_list))    

print(check_num(1,10)) 
