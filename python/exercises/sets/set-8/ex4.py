'''
4. Write a function to take a dict as argument. If the dict-val is the divisible bydict-key then filter, 
   add to new dict.Finally return the new dict
        Example : 
            testDict={10:20, 3:30, 4:16,90:100,20:30,11:23,17:44,20:400}
            result=func_exec(testDict)
            print(result)
            Expected Output : {10:20,3:30,4:16,20:400}
            Reason: 
                20 is divisible by 10
                30 is divisible by 3
                16 is divisible by 4
                400 is divisible by 20
'''
def check_dic(org_dic):
    new_dic={}
    for i,j in org_dic.items():
        if (j%i==0):
            new_dic[i]=j
    return new_dic
print(check_dic({10:20, 3:30, 4:16,90:100,20:30,11:23,17:44,20:400}))        
