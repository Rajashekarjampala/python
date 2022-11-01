# Numbers print with reverse

def check_range(n1,n2,stp):
    new_list=[]
    # range is taken reverse and -2 is indicates reverse step size
    for i in range(10,0,-2):
        new_list.append(i)
    return new_list

print(check_range(10,0,2))        

