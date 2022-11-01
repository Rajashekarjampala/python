# Using **kwargs to pass the variable keyword arguments to the function 

def intro(**data):
    
    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Raj", Lastname="Shekar", Age=25, Phone=1234567890)