'''
Write a function to take a list and StringX as arguments. Find the elements in the list
     whose length is >er than of StringX. Add to new list and return.
    Example :
    ---------
        listA=["hello","world","science","maths","Python"]
        stringX="Bigger String"
        result=func_exec(listA,stringX)
        print(result)
        Expected Output : []
        Reason: Length of stringX is 13. All elements in the list have length <13
    Example :
    ---------
        listA=["hello","world","science"]
        stringX="Bigger String"
        result=func_exec(listA,stringX)
        print(result)
        Expected Output : []
        Reason: Length of stringX is 13. All elements in the list have length <13
    Example :
    ---------
        listA=["hello","world","science","Physics","Atoms","Google","Hello World!"]
        stringX="Big String"
        result=func_exec(listA,stringX)
        print(result)
        Expected Output : ["Hello World!"]
        Reason: Length of stringX is 10. Length of "Hello World!" is 12
'''
def check_word(listA,strX):
    new_list=[]
    for ele in listA:
        if (len(ele)>len(strX)):
            new_list.append(ele)
    return new_list

# Execution   
listA=["hello","world","science","Physics","Atoms","Google","Hello World!"]
stringX="Big String"
result=check_word(listA,stringX)
print(result) 

