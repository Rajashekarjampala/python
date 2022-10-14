'''Write a function to take a dict, number X as arguments.
If the dict key is > number X, then add it to new dict. Finally iterate and return the new dict.'''
#define function
def num_gre(org_dict,x):

    #define new dictionary
    new_dict={}
    #values() gives list of tuples 
    #iterates keys and values simantously
    for i,j in org_dict.items():
        #checking for thr condition is the element is greater than the value x
        if (i>x):
            #upadting new dictionary
            new_dict[i]=j
    #finlly returns new dictionary        
    return new_dict

#calling function    
x=num_gre({11:1,9:2,8:3,0:4,76:5,5:6,4:7,3:8,922:9,911:10},50)
print('final output{}'.format(x))   
