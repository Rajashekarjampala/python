'''
3. Write a function to take a list. From the list find the number that occurs most number of times.
    Example :
        listA=[10,20,30,40,50,60,100,11,12,13]
        result=func_exec(listA)
        print(result)
        Expected Output : []
    Example :
        listA=[10,21,30,41,50,500,100,11,12,13,21]
        result=func_exec(listA)
        print(result)
        Expected Output : [21,]
    Example :
        listA=[10,21,30,41,50,50,100,11,12,13,21]
        result=func_exec(listA)
        print(result)
        Expected Output : [21,50]
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY.  
Solution Steps:
**************
Iterate the orginal list 
  Check condition for most repeated element in the list and remove the duplicate numbers
      If yes:
        add the new list
      else:
        continue the loop  
Add finally retun the new list
'''
# Define function
def check_repeat(listA):
  # define empty dic
  new_dict={}
  #Iterate the original list
  for i in listA:
    # count the numbers from original list
    count=listA.count(i)
    # count more than one element
    if(count>1):
      # Update new dic
      new_dict[i]=count
      
  # Define new list    
  new_list=[]
  # from new dic store the values in variable
  val=new_dict.values()
  # Iterate the new dic
  for k,v in new_dict.items():
      # find the max repeat num from dic (dic value)
      if(v==max(val)):
        # repeat numbers add to new list
        new_list.append(k)
  # Finally return the new_list      
  return new_list      

# Execution
#calling function
#Testcase 1
result=check_repeat([10,20,30,40,50,60,100,11,12,13])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_repeat([10,21,30,41,50,500,100,11,12,13,21])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_repeat([10,21,30,41,50,50,100,11,12,13,21,50])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_repeat([1,2,3,4,5,6,7,8,9,10,1,2,1])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_repeat([100,200,1000,400,500,100,800,900,1000])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_repeat([23,25,23,24,25,26,27,28,25,30])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_repeat([90,91,92,93,94,95,96,97,98,99,100])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_repeat([44,22,33,44,55,66,44,88,44,100])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_repeat([25,35,45,55,65,75,85,95,105,115])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_repeat([121,221,321,421,521,621,121,821,921])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#


