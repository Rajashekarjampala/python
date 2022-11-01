# Write python programme for a below 18 years person not eligible for vote
# Function with arg

def check_vote(age):
    if age >= 18: 
        return ('eligible for vote')
    else:
         return ('Not eligible for vote')
                  
#age = int(input("Enter your age: ")) 
result=check_vote(30)    
print(result)

# Write python programme for a below 18 years person not eligible for vote
# Function without arg

'''def check_vote():
    
    age = int(input("Enter your age: ")) 
    
    if age >= 18: 
        return ('eligible for vote')
    else:
         return ('Not eligible for vote')
                  

result=check_vote()    
print(result)'''