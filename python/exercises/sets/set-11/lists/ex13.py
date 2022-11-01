'''
Write a function to take a list argument. Find the element that has greatest length.
	Example :
		listA=["hello","world","science","maths","Python"]
		Expected Output : ["science"]
		Reason: length of science -> 7
'''

a=['rakesh','raj','python','developer']
great=[]
for i in a:
  great.append(len(i))
for j in a:
  if(len(j)==max(great)):
    print(j)


a=['rakesh','raj','python','developer']
ele_len=len(a[0])
ele_name=a[0]
for i in a:
  if(len(i)>ele_len):
    ele_len=len(i)
    ele_name=i
print(ele_name)
    