'''1. Write a function to take a list, numX, numY as arguments.
    Filter all the numbers from the list that are >numX and <numY and add to new list.
    Finally return the new list.
    Example :
        listA=[10,20,30,40,50,60,100,11,12,13]
        numX=45
        numY=55
        result=func_exec(listA)
        print(result)
        Expected Output : [50]
        Reason: 50 is >er than numX 45 and <er than numY 55
    Example :
        listA=[10,20,30,46,52,60,54,11,12,13]
        numX=45
        numY=55
        result=func_exec(listA)
        print(result)
        Expected Output : [46,52,54]
        Reason: 46 is >er than numX 45 and <er than numY 55
        Reason: 52 is >er than numX 45 and <er than numY 55
        Reason: 54 is >er than numX 45 and <er than numY 55
    Example :
        listA=[10,20,30,46,52,60,54,11,12,13]
        numX=450
        numY=550
        result=func_exec(listA)
        print(result)
        Expected Output : []
        :param org_list: Original list passed by the User
        :param numy: Number y passed by the User. Type is INT.
        :param numy: Number y passed by the User. Type is INT.
        :return: New list with filtered values ONLY.  

    Solution Steps:
    **************
    Iterate the Orginal list
    Find the numbers greter than numberx
    Find the numbers less than numbery
    Pic the numbers between numberx and numbery
    Filter numbers are add to new list and retun new list

'''

def check_func(org_list,numx,numy):
    new_list=[]
    for i in org_list:
        if (i>numx and i<numy):
            new_list.append(i)
    return new_list

print(check_func([10,20,30,40,50,60,100,11,12,13],45,55))            