#repeatable elements

listA=[1,2,3,2,6,78,9,1,1]
new_dict={}
for i in listA:
  count=listA.count(i)
  if(count>1):
    new_dict[i]=count
print(new_dict)
  