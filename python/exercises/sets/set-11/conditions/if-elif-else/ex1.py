# if-elif-else Statement: 

# The elif statement check multiple expressions 
# and executes block of statements wherever the condition returns as True.
# If any of the expression not returns as true, then it executes the else block code

def check_num(x,y):
    if x > y:
        return("x is greater than y")
    elif x < y:
        return("x is less than y")
    else:
        return("x is equal to y")

print(check_num(20,30))        