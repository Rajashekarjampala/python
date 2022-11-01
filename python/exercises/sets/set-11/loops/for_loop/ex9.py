# Calculate the square of all numbers between  given range
# Function without arg
'''def check_squ():
    num1=int(input("Enter a starting number: "))
    num2=int(input("Enter a ending number: "))
    new_list=[]
    for i in range(num1, num2 + 1):
        new_list.append(i*i)
    return new_list
print(check_squ())'''      

# Functions witharg
def check_squ(num1,num2):
    new_list=[]
    for i in range(num1, num2 + 1):
        new_list.append(i*i)
    return new_list
print(check_squ(int(input("Enter a starting number: "),int(input("Enter a ending number: ")))))