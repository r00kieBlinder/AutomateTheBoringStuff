# 415-555-4242

def isPhoneNumber(text):
    if len(text) != 12: 
        return False
    for i in range(0, 3): 
        if not text[i].isdecimal():
            return False 
    if text[3] != '-':
        return False 
    if i in range(4, 7):
        if not text[i].isdecimal():
            return False 
    if text[7] != '-':
        return False 
    if i in range(8, 12):
        if not text[i].isdecimal():
            return False 
    return True 

'''
# To make it more dynamic check the code under this code 

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))
'''


n = input("Check if it's a phone number -> ")

n = str(n)

if isPhoneNumber(n):
    print('Yes. It is a phone number!')
else:
    print('Sorry! It is not a phone number. Try again.')

