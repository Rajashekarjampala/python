# For_Loop :
# The for loop provides to repeat a task until a particular condition is true.
# For loop is known as a determine exactly how many times the loop will repeat.
# The number of times the loop has to be executed can be determined logic of the loop

# Program to find the sum of all numbers stored in a list

def check_sum(*numbers):
    # variable to store the sum
    sum = 0
    # iterate over the list
    for i in numbers:
        sum = sum+i
    return(sum)

print("The sum is", check_sum(1,2,3,4,5))
