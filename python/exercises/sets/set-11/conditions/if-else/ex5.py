# write program to a number divisible 7 or not

def check_num(num):

    if (num%7==0):
        return("number divisible by 7 ")
    else:
        return("number not divisible by 7 ")

print(check_num(42))