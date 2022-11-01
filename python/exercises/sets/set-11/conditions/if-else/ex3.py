'''4. Write a program to determine whether the character entered is a vowel or not.'''

def check_cha(cha):
  if (cha in "aeiouAEIOU"):
    return('vowel')
  else:
    return("not vowel") 

print(check_cha("a"))    