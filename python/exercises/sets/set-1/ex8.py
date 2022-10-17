'''
8.From the list pick the elements that are not EVEN. Add those elements to new list. 
Finally print the new list.
'''
# Define original list
org_list=[11,100,127,99,125,331,990,23,68,10]
# Define new list list
new_lst=[]
# Iterate the list
for i in org_list:
    # To check the number is odd(not even)
    if(i%2!=0):
        # Add to the new list
        new_lst.append(i)
# Finally print the new list        
print(new_lst)