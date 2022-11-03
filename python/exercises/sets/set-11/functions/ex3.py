'''write a python function to Take a dict as argument and check whether the sum of the key and value is prime .
Add to new dic and Return the key and value '''

def check_num(dic):
  new_dic={}
  for k,v in dic.items():
    sum=k**2+v**2
    if (sum>=2):
        for i in range(2,sum):
            if (sum%i==0):
                break
        else:
            new_dic[k]=v 

  return new_dic        
print(check_num({10:20,3:30,4:40,90:100,20:30,11:23,17:44,2:5}))      
