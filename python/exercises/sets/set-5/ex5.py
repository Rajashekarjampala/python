'''
5. Write a function to take a dict as argument. Sort the dict by values and return the dict.
    Example : 
            testDict={1:4,10:20,3:40,4:7,60:11,12:9}
            result=func_exec(testDict)
            print(result)
            Expected Output : {1:4,4:7,12:9,60:11,10:20,3:40}
            :param org_dic: Original dictionary passed by the User
            :return: New dic with filtered values ONLY
Solution Steps:
**************
Define the the function 
  We can take one empty dictionary
  Sort the dictionary value and store in variable
  Iterate the original dictionary
  Sorted values are add to the empty dictionary 
  Return the empty dictionary 
Print empty dictionary               
'''
#This function returns new sorted dictionary by values
def sort_value(org_dic):
    
    #define empty dictionary
    new_mapper={}
    #values() method gives list of values
    #stores sorted list of values
    _val=sorted(org_dic.values()) 
    #iterates values one by one
    for _key in _val:    
        #iterates keys from original dict one by one
        for _val in org_dic: 
            #checking for values and keys if condition true it adds to new dict. 
            if(_key==org_dic[_val]):   
                #add key-value pair to new dictionary
                new_mapper[_val]=_key  
    # finally return the new dic                         
    return new_mapper               

#calling function
#Testcase 1
result=sort_value({1:4,10:20,3:4,4:7,60:11,12:9})
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=sort_value({2:4,5:3,3:1,4:8,9:4,7:2})
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=sort_value({32:3,42:5,75:3,83:13,63:75,61:23})
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=sort_value({3:2,4:1,45:31,72:73,52:31,53:31})
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=sort_value({3:5,4:3,5:8,9:5,9:2,12:17})
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=sort_value({42:21,57:31,75:31,73:36,83:31,9:5})
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=sort_value({12:21,16:61,14:41,17:71,13:31,15:51})
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=sort_value({2:3,6:7,4:5,7:8,5:6,3:4})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=sort_value({9:5,8:4,7:3,6:2,5:1,10:7})
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=sort_value({18:81,17:71,19:91,27:72,22:22,32:23})
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#