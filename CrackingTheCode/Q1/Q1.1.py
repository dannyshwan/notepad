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

string1 = "abcdefg"
string2 = "abcdefg1123"

print(isUnique(string1)) #Should print True
print(isUnique(string2)) #Shoud print False