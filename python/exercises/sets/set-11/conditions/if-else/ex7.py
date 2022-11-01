# Write program to a number is divisible by both 2 and 3

def check_num(num):

    if (num%2==0 and num%3==0):
        return("Number is divisible by 2 and 3")
    else:
        return("Number is not divisible by 2 and 3")

print(check_num(25))