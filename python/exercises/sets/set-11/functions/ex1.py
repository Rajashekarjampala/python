# Using *args to pass the variable length arguments to the function

def num_sum(*num):
    sum = 0    
    for i in num:
        sum = sum + i
    return sum

print(num_sum(1,2,3,5,6))