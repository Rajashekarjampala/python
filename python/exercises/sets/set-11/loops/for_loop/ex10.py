# Calculate the cube of all numbers between given numbers

def check_cube(num1,num2):
    cube_list=[]
    for i in range(num1,num2):
        cube_list.append(i**3)
    return cube_list

print(check_cube(1,10))        