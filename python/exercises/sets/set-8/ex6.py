'''6. Write a function to take 3 lists, numX, numY as arguments.
      If the sum of elements in the indexes is > er sum of numX + numY, then add to new list.
    Finally return the new list.
    Note: You must execute only if the lists are of same length.
    Example :
        listA=[10,20,30,40,50]
        listB=[1,2,3,4,5]
        listC=[100,150,200,250,300]
        numX=150
        numY=100
        result=func_exec(listA)
        print(result)
        Expected Output : [[40,4,250],[50,5,300]]
        Reason: 
            sum of (numX + numY) = 250
            -    sum of ([40,4,250]) is > er than sum of (numX + numY)
            -    sum of ([50,5,300]) is > er than sum of (numX + numY)
    Example :
        listA=[10,20,30,40,50]
        listB=[1,2,3,4,5]
        listC=[100,150,200,250,300]
        numX=50
        numY=100
        result=func_exec(listA)
        print(result)
        Expected Output : [[20,2,150], [30,3,200], [40,4,250],[50,5,300]]
        Reason:
            sum of (numX + numY) = 150 
            -    sum of ([20,2,150]) is > er than sum of (numX + numY)
            -    sum of ([30,3,200]) is > er than sum of (numX + numY)                        
            -    sum of ([40,4,250]) is > er than sum of (numX + numY)
            -    sum of ([50,5,300]) is > er than sum of (numX + numY)
    Example :
        listA=[10,20,30,40,50]
        listB=[1,2,3,4,5]
        listC=[100,150,200,250,300]
        numX=500
        numY=100
        result=func_exec(listA)
        print(result)
        Expected Output : []
        Reason: 
           sum of (numX + numY) = 600
           Sum of values in the indexes are < 600
'''
def check_list(l1,l2,l3,x,y):
    for i,j,k in zip(l1,l2,l3):
    
