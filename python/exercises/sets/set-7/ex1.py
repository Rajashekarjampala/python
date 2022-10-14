'''
1.  Write a function to take a list. Filter all the even numbers from the ODD indexes. Remove duplicates.
    Example :
        listA=[10,20,30,40,50,60,100,11,12,13]
        result=func_exec(listA)
        print(result)
        Expected Output : [20,40,60]
    Example :
        listA=[10,21,30,41,50,50,100,11,12,13]
        result=func_exec(listA)
        print(result)
        Expected Output : [50]
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY. 

Solution Steps:
***************
  Iterate the original list
    From the list pic the ODD indexes
    From the ODD indexes checking number is even numbers 
    checking for number already not present in new list
      if number even:       
          number add to new list
      else:
        continue loop        
  Finally return new list
  '''

# Function define filter the all the even numbers from the ODD indexes
def check_eve_ind(org_list):

  #define new list
  new_list=[]
  #loop produce odd numbers from 1 to size of the original
  for i in range(1,len(org_list),2):    
    #checking for number is even
    if(org_list[i]%2==0):
      #checking for number is not present in new list
      if(org_list[i] not in new_list):
        #addiing number to new list
        new_list.append(org_list[i])
  #finally reterns new list
  return new_list

# Execution
testorg_list=[10,20,30,40,50,60,100,11,12,13]
#function calling
result=check_eve_ind(org_list=testorg_list)
#finally print result
print("Final Result is :: {} ".format(result))    


