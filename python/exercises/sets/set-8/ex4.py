'''
4. Write a function to take a dict as argument.
If the dict-val is the divisible by dict-key then filter, add to new dict.
Finally return the new dict.
      
  Example 1 : 
      testDict={10:20, 3:30, 4:16,90:100,20:30,11:23,17:44,20:400}
      result=func_exec(testDict)
      print(result)
      Expected Output : {10:20,3:30,4:16,20:400}
      
      Reason: 
            20 is divisible by 10
            30 is divisible by 3
            16 is divisible by 4
            400 is divisible by 20
      :param org_dict: Original dictionary passed by the User
      :return: New dictionary with filtered values ONLY.  

  Solution Steps:
  **************
  Take a dict and iterate keys and values simantanously
  checking for value is divisible by key
    if Yes:
      add key and value to new dict
    else
      continue loop
  Finally return new dict              
'''
#define function
def check_div(org_dict):
    #deine new dict
    new_dict={}
    #iterates keys and values simantanously
    for _key,_value in org_dict.items():
      #checking for is value is divisible by key
      if(_value%_key==0):
        #add key and value to new dict
        new_dict[_key]=_value
    #finally return new dict    
    return new_dict

#calling function
#Testcase 1
result=check_div({10:20, 3:30, 4:16,90:100,20:30,11:23,17:44,20:400})
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_div({20:5,5:3,30:15,4:8,9:4,7:2})
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_div({32:3,42:5,75:3,83:80,63:75,60:23})
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_div({5:125,410:10,45:31,72:73,520:310,53:31})
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_div({300:50,4:3,500:80,9:5,9:2,12:17})
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_div({42:21,517:31,750:35,73:36,830:83,9:5})
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_div({121:11,6:61,14:41,17:71,13:31,15:51})
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_div({2:3,6:7,4:5,7:8,5:6,3:4})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_div({9:5,8:4,7:3,6:2,5:1,10:7})
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_div({18:81,17:71,19:91,27:72,22:22,32:23})
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#