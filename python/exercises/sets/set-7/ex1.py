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
#calling function
#Testcase 1
result=check_eve_ind([10,20,30,40,50,60,100,11,12,13])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_eve_ind([10,21,30,41,50,50,100,11,12,13])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_eve_ind([11,12,13,14,15,16,17,18,19,20])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_eve_ind([1,2,3,4,5,6,7,8,9,10])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_eve_ind([100,200,300,400,500,600,700,800,900,1000])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_eve_ind([21,22,23,24,25,26,27,28,29,30])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_eve_ind([90,91,92,93,94,95,96,97,98,99,100])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_eve_ind([11,22,33,44,55,66,77,88,99,100])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_eve_ind([25,35,45,55,65,75,85,95,105,115])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_eve_ind([121,221,321,421,521,621,721,821,921])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#


