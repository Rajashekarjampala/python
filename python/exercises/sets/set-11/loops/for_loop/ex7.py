# Calculate Tables

def check_tab(n):
    # stop: 11 (because range never include stop number in result)
    # run loop 10 times
    table_list=[]
    for i in range(1,11):

        # multiplying number with i value
        print('{} * {} = {}'.format(n,i,n*i))
check_tab(2)