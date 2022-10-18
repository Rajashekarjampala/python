'''
5. Write a function to take a dict and number X as argument. 
Find the key,value pairs that are both divisible by number X
    Example : 
            testDict={10:20, 3:30, 4:40,90:100,20:30}
            numX=10
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {10:20,90:100,20:30}
            :param org_dic: Original dictionary passed by the User
            :param numX: Number X passed by the User. Type is INT.
            :return: New dic with filtered values ONLY
            
Solution Steps:
**************
Iterate new dictionary of keys and values
Check if condition is  key and value both divisible by numberX 
  If Yes:
    add to new dictionary
  else:
    continue loop
Finally return the new dictionary      
'''  

# This function is defines the key and value (item) divisible by a num            
def check_div(org_dic,numx):
  # define new empty dictionary
  new_dic={}
  # iterate the key,and value from the orginal dictionary
  for _key,_value in org_dic.items():
    # To check the condition if key and value divisible by numberx
    if (_key%numx==0 and _value%numx==0):
      # Update to the new ditionary
      new_dic[_key]=_value
  # finally return the new dictionary
  return new_dic

# Execution
#calling function
#Testcase 1
result=check_div({10:20, 3:30, 4:40,90:100,20:30},10)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_div({22:44,5:3,33:11,4:8,9:4,77:22},11)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_div({32:3,42:5,75:3,83:13,63:75,61:23},15)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_div({3:2,40:10,45:31,72:73,52:31,55:30},5)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_div({3:5,4:3,5:8,9:5,9:2,12:17},12)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_div({42:21,57:31,75:31,73:36,83:31,9:12},3)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_div({12:21,16:61,14:41,17:34,13:31,68:51},17)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_div({21:42,6:7,4:5,7:8,5:6,3:4},21)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_div({9:5,8:4,7:3,6:2,5:1,10:7},8)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_div({180:810,17:71,19:91,270:720,22:22,32:23},100)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#