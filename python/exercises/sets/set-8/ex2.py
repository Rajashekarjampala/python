'''
    2. Write a function to take a list argument. Find the elements that has greatest length.

    Example 1 :
        listA=["hello","world","science","maths","Python"]
        result=func_exec(listA)
        print(result)
        Expected Output : ["science"]
        Reason: length of science -> 7

    Example 2 :
        listA=["hello","world","science","maths","Pythonics"]
        result=func_exec(listA)
        print(result)
        Expected Output : ["Pythonics"]
        Reason: length of Pythonics -> 9

    Example 3 :
        listA=["hello","world","today"]
        result=func_exec(listA)
        print(result)
        Expected Output : []
        Reason: All lengths are same.
        Length of hello -> 5
        Length of world -> 5
        Length of today -> 5
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY.  
        
    Solution Steps:  
    **************
    Take original list and iterate
        Store sizes of words in a list 
        checking if the word size is greater than remaining words
        if yes:
            add to new list
        else:
            continue loop
    check for new list contains only one word
    if yes:
        return new list
    else:
        retuen empty list []                
'''

#define function 
def check_greater(org_list):
    #define new list 
    new_list=[]
    #define list to store lengths of elements in orginal list
    len_list=[]
    #iterate original list
    for i in org_list:
        #adding lengths   to lengths list
        len_list.append(len(i))
    #iterate orginal list
    for j in org_list:
        if(len(j)==max(len_list)):
            new_list.append(j)    
    #checking for is element in new list one ,if new list contains more than one returns empty list
    if(len(new_list)==1):
        return new_list
    else:
        return [] 
 #calling function  
#Testcase 1
result=check_greater(["hello","world","science","maths","Python"])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_greater(["hello","world","science","maths","Pythonics"])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_greater(["hello","world","today"])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_greater(["prashanth","shekar","sravan","goutham","prasad","sraavi"])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_greater(["airtel","vodafone","idea","jio","bsnl","mahesh"])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_greater(["india","srilanka","america","south africa","afganisthan"])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_greater(["cat","dog","elephant","fox","rabbit"])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_greater(["hyderabad","miyapur","kukatpally","sangareddy","patancheru"])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_greater(["mobile","laptop","redmi","realme","vivo"])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_greater(["book","pen","pencile","niddle","writteing"])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#