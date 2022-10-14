'''
5. Write a function to take a dict as argument. Return the key that has max value.
    Example : 
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
'''
def check_dic(org_dic):
    new_dic={}
    for i,j in org_dic.items():
        if max(org_dic.values):
            new_dic[i]=j
    return new_dic
print(check_dic({10:20, 3:30, 4:16,90:100,20:30,11:23,17:44,20:400}))        
