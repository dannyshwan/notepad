'''
Checks if a string is a permutation of the other
'''

def CheckIfPermutation(str1, str2):
    charArray1 = list(str1)
    charArray2 = list(str2)

    charArray1.sort()
    charArray2.sort()

    if charArray1 != charArray2:
        return False
    
    return True

string1 = "cat"
string2 = "act"
string3 = "tap"

print(CheckIfPermutation(string1, string2)) #Should print True
print(CheckIfPermutation(string1, string3)) #Should print False