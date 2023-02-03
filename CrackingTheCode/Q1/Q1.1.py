'''
Checks to see if all characters in a string are unique
Solved by: Daniel Shwan
'''

def isUnique(str):
    charArray = list(str)
    charArray.sort

    for i in range(0,len(charArray)):
        if(((i+1) != len(charArray)) and (charArray[i] == charArray[i+1])):
            return False
    return True


# option two (Possibly More Pythonic Way)
# Converts the string to a set
# if the lenght if the set == length of the initial string
# therefore all the chars in the initial strings are unique else there is a repetition
def _isUnique(str):
    chars = set(str)
    return True if len(chars) == len(str) else False


string1 = "abcdefg"
string2 = "abcdefg1123"

print(isUnique(string1)) #Should print True
print(isUnique(string2)) #Shoud print False

# Self test for the new version
print(_isUnique(string1)) #Should print True
print(_isUnique(string2)) #Should print False
