inputA = input("Please enter a string to know how many letters is uppercase and how many is lowercase: ")

def up_lowNums(string):
    uppercaseNum = 0
    lowercaseNum = 0
    
    for letters in string:
        if letters.isupper() == True:
            uppercaseNum += 1
        elif letters.islower() == True:
            lowercaseNum += 1
    return "No. of Uppercase characters: {} and the No. of the Lowercase characters: {}".format(uppercaseNum, lowercaseNum)
    
up_lowNums(inputA)
