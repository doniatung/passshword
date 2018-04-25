UC_LETTERS = "ABCDEFGHIJKLNOPQRSTUVWXYZ"
NUMS = "1234567890"
NONALPHNUM = ".?!&#,;:-_*"

def threshold(password):
    return checkNumbers(password) & checkLetters(password)

def checkNumbers(password):
    word = [1 if x in NUMS else 0 for x in password]
    num = word[0]
    for each in word:
        if(num != each):
            return True
    return False

def checkLetters(password):
    letters = [1 if x in UC_LETTERS else 0 for x in password]
    num = letters[0]
    for each in letters:
        if (num != each):
            return True
    return False

def checkAlph(password):
    word = [1 if x in NONALPHNUM else 0 for x in password]
    num = word[0]
    for each in word:
        if (num != each):
            return True
    return False

def rating(password):
    rating=0
    if (checkNumbers(password)):
        rating += 3
    if (checkLetters(password)):
        rating += 3
    if (checkAlph(password)):
        rating += 3
    return rating


print threshold("helLo1") #True
print threshold("sapghe") #False
print threshold(";agoeE1oubawu") #True
print threshold("owingeE")#False
print threshold("woigen2")#False

print rating("a;lnoeb2345")
print rating("Drag0n123")
