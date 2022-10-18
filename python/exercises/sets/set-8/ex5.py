'''
5. Write a function to take a dict as argument. Return the key that has max value.
        
    Example 1 : 
            testDict={10:20, 3:30, 4:16,90:100,20:31,11:23,17:44,20:400}
            result=func_exec(testDict)
            print(result)
            Expected Output : {20:400} 
            Reason:            
                400 is > 20
                400 is > 30
                400 is > 16
                400 is > 100
                400 is > 31
                400 is > 23
                400 is > 44
            :param org_dict: Original dictionary passed by the User
            :return: New dictionary with filtered values ONLY.      
                
    Solution steps:
    **************
    Take original dict and iterate key-value simantanously
        store values in _values
        checking for current key-value is greater than remaining 
        if Yes:
            add key-value to new dict
        else:
            continue loop
    Finally return new dict
'''
#define funtion
def check_max(org_dict):
    
    #define new dict
    new_dict={}
    #stores values in a list
    _values=org_dict.values()
    #iterates keys and values simantanously from original dict
    for _key,_value in org_dict.items():
        #checking for current key-value is greater than reamaining key-values
        if(_value==max(_values)):
            #updating new_dictionary
            new_dict[_key]=_value
   #finally returns new dict
    return new_dict

#calling function
#Testcase 1
result=check_max({10:20, 3:30, 4:16,90:100,20:31,11:23,17:44,20:400})
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_max({20:5,5:3,30:15,4:8,9:4,7:2})
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_max({32:3,42:5,75:3,83:80,63:75,60:23})
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_max({5:125,410:10,45:31,72:73,520:310,53:31})
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_max({300:50,4:3,500:80,9:5,9:2,12:17})
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_max({42:21,517:31,750:35,73:36,830:83,9:5})
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_max({121:11,6:61,14:41,17:71,13:31,15:51})
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_max({2:3,6:7,4:5,7:8,5:6,3:4})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_max({9:5,8:4,7:3,6:2,5:1,10:7})
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_max({18:81,17:71,19:91,27:72,22:22,32:23})
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#