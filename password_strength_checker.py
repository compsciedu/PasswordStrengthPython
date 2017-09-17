#Password Strength Checker
#GCSE Computer Science
def checklength(password:str):
    length = len(password)
    return length

def checkcase(password):
    uppercount = 0
    lowercount = 0
    for letter in password:
        if letter.isupper():
            uppercount=+1
        if letter.islower():
            lowercount=+1
    return uppercount, lowercount

def checknumber(password):
    numbercount = 0
    for letter in password:
        if letter.isnumeric():
            numbercount=+1
    return numbercount

def checksymbol(password):
    symbolcount = 0
    symbol_list = ["!","@"]
    for letter in password:
        if letter in symbol_list:
            symbolcount =+1
    return symbolcount

password = input("Enter password ")
length = checklength(password)
uppercount, lowercount = checkcase(password)
numbercount = checknumber(password)
symbolcount = checksymbol(password)
print(length)
print(uppercount)
print(lowercount)
print(numbercount)
print(symbolcount)


