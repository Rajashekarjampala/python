# if –else Statement:
# If the expression is True, statement block 1 is executed and statement block 2 is skipped. 
# If the expression is False, statement block 2 is executed and statement block 1 is ignored.

def check_num(x,y):

	if x < y:
		return("x is less than y")
	else:
		return("x is equal to or greater than y")

print(check_num(10,20))
