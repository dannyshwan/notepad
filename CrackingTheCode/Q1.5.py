'''
Check if two strings are different by one edit
Solved by: Daniel Shwan
'''

def OneAway(str1, str2):

    editStr1 = str1
    editStr2 = str2

    if str1 == str2:
        return True

    for i in range(0,len(str1)):
        
        char = str1[i]

        editStr1 = editStr1.replace(char,'')
        editStr2 = editStr2.replace(char,'')

    if (len(editStr1)-len(editStr2)>1) or (len(editStr2)-len(editStr1)>1):
        return False

    return True

print(OneAway("pales", "pale")) #Should print True
print(OneAway("pale", "ple")) #Should print True
print(OneAway("pale", "bale")) #Should print True
print(OneAway("pale", "bake")) #Should print False