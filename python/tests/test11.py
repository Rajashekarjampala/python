'''
Write a function to take a dictionary, numX as arguments.
    If the dict keys & dict values are BOTH DIVISIBLE by numX then add it to new dict. (Use dict update method)
    Sort the key by Keys.
    Return new dict.
    Example : 
    ---------
            testDict={1:4,10:20,3:40,4:7,60:11,12:9}
            numX=3
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {12:9}
    Example : 
    ---------
            testDict={1:4,10:20,3:40,4:7,60:11,12:9}
            numX=13
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {}
    Example : 
    ---------
            testDict={4:44,12:20,3:40,4:7,60:11,12:9}
            numX=4
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {4:44,12:20}
'''
def check_div(dic,numX):
    new_dic={}
    for _key,_val in dic.items():     
        if (_key%numX==0 and _val%numX==0):            
            #new_dic[_key]=_val
            new_dic.update({_key:_val})
    return sort_by_key(new_dic),sort_by_val(new_dic),new_dic

def sort_by_key(dic):
    new_dic={}
    for _key in sorted(dic.keys()):
        new_dic.update({_key:dic[_key]})
    return new_dic

def sort_by_val(dic):
    new_dic={}
    val_var=sorted(dic.values())
    for _key,_value in dic.items():
        for _val in val_var:
            if (_val==_value):
                new_dic.update({_key:_value})   
    return new_dic

# Execution
testDict={30:9,1:4,10:20,3:40,4:7,60:11,12:9,15:30}
numX=3
result=check_div(testDict,numX)
print(result)  

