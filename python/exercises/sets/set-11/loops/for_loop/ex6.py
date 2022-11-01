# Using list as range 
#listA= [10,20,30,40,50,60,70,80,90,100]

def check_range(listA):
    new_list=[]
    for i in range(len(listA)):
        new_list.append(listA[i])
    return new_list

print(check_range([10,20,30,40,50,60,70,80,90,100]))    