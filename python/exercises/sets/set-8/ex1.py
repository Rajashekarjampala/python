'''
1. Write a function to take a list, numX, numY as arguments.
Filter all the numbers from the list that are >numX and <numY and add to new list.
Finally return the new list.

    Example 1 :
        listA=[10,20,30,40,50,60,100,11,12,13]
        numX=45
        numY=55
        result=func_exec(listA)
        print(result)
        Expected Output : [50]
        Reason: 50 is >er than numX 45 and <er than numY 55

    Example 2 :
        listA=[10,20,30,46,52,60,54,11,12,13]
        numX=45
        numY=55
        result=func_exec(listA)
        print(result)
        Expected Output : [46,52,54]
        Reason: 46 is >er than numX 45 and <er than numY 55
        Reason: 52 is >er than numX 45 and <er than numY 55
        Reason: 54 is >er than numX 45 and <er than numY 55

    Example 3 :
        listA=[10,20,30,46,52,60,54,11,12,13]
        numX=450
        numY=550
        result=func_exec(listA)
        print(result)
        Expected Output : []
        :param org_list: Original list passed by the User
        :param numx: Numberx passed by the User. Type is INT.
        :param numy: Numbery passed by the User. Type is INT.
        :return: New list with filtered values ONLY.  

    Solution Steps:
    **************
    Take a original list and iterate original list     
    Check if number is greater than number X and number less than number Y
        if yes:
            add to new list
        else:
            continue lopp  
    Finally return new list              
'''
#define function
def check_num(org_list,numX,numY):
    #define new list
    new_list=[]
    #iterate elements from original list one by one
    for i in org_list:
        #checking for element is greater than x and less than y
        if(i>numX and i<numY):
            #adding element to new list
            new_list.append(i)
    #finally return new list
    return new_list

#calling function
#example1
x=check_num([10,20,30,40,50,60,100,11,12,13],45,55)
print('final output : {}'.format(x))        

#example2
y=check_num([10,20,30,46,52,60,54,11,12,13],45,55)
print('final output : {}'.format(y))  

#example3
z=check_num([10,20,30,46,52,60,54,11,12,13],450,550)
print('final output : {}'.format(z))  

#example4
s=check_num([10,20,30,46,52,60,54,11,12,13],20,30)
print('final output : {}'.format(s))