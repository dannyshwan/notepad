'''
Check if two strings are different by one edit
Solved by: Daniel Shwan
'''

def OneAway(str1, str2):

    difference = 0
    stringLength1 = len(str1)
    stringLength2 = len(str2)

    if str1 == str2:
        return True
    
    elif (stringLength1 - stringLength2 > 1) or (stringLength2 - stringLength1 > 1):
        return False

    for i in range(0,stringLength1):
        
        if i == stringLength2:
            return True
        elif (str1[i] != str2[i]):
            difference += 1
        
        if difference > 1:
            return False
    
    return True

print(OneAway("pales", "pale")) #Should print True
print(OneAway("pale", "ple")) #Should print True
print(OneAway("pale", "bale")) #Should print True
print(OneAway("pale", "bake")) #Should print False