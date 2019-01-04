'''
Given a string, return the basic string compression using the counts of repeated characters
Solved by: Daniel Shwan
'''

def StringCompression(string):
    
    newStr = ""
    char = string[0]
    count = 0

    for i in range(0,len(string)):
        
        if i+1 == len(string):
            if char != string[i]:
                newStr += char + str(count) + string[len(string)-1] + "1"
            else:
                newStr += char + str(count+1)

        elif char != string[i]:
            newStr += char + str(count)
            char = string[i]
            count = 1

        else:
            count += 1

    #Returns original string if length of "compressed" string is not difference to the original
    if len(newStr) == len(string):
        return string

    return newStr

print(StringCompression("abcccccaaa")) #Should print "a2b1c5a3"