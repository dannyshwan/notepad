'''
Checks to see if a given string is a permutation of a palindrome
Solved by: Daniel Shwan
'''

def PalindromePermutation(str):

    even = True
    middleChar = 0
    charsInString = []

    str = str.replace(" ", "")
    str = str.lower()

    if len(str)%2 != 0:
        even = False

    for char in str:
        if char not in charsInString:
            charsInString.append(char)
            
    for char in charsInString:
        occurence = charOccurence(char, str)

        if(occurence%2 != 0):
            if (middleChar == 0) and (occurence == 1) and not even:
                middleChar += 1
            
            else:
                return False
    
    return True

def charOccurence(charOfInterest, str):

    occurence = 0
    for char in str:
        if char == charOfInterest:
            occurence += 1
    
    return occurence

print(PalindromePermutation("Tact Coa")) #Should print True
print(PalindromePermutation("taco cat")) #Should print True
print(PalindromePermutation("atco cta")) #Should print True
print(PalindromePermutation("ccat oct")) #Should print False