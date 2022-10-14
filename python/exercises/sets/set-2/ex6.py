'''
    Write a function to take a list, number X, number Y as argument.
    If the element is even then multiply that element by number X, 
    if the element is odd then multiply that element by number Y. Finally return the new list.

'''

#define function
def mult_num(org_list,x,y):
    
    #define new list
    new_list=[]
    #iterates elements from orginal list one by one
    for i in org_list:
        #checking for the element even
        if (i%2==0):
            #adding to new list
            #mutiply element by x
            new_list.append(i*x)
        else:
            #multiply by y
            new_list.append(i*y)
    #final return new list        
    return new_list

#calling function    
x=mult_num([2,5,8,9,3,4],2,3)
print('final output :-  {}'.format(x))             