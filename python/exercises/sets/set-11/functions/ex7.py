'''write a function to take argument as dictionary.
    iterate the dictionary and find the elements which key is greater than value
    add to new dictionary and return new dictionary

    Example:
        result={1:10,20:2,50:50,30:60,70:7}
        expected output={20:2,70:7}
'''
def check_num(dic):
    new_dic={}
    for k,v in dic.items():
        if (k>v):
            new_dic[k]=v
    return new_dic

print(check_num({1:10,20:2,50:50,30:60,70:7}))            
