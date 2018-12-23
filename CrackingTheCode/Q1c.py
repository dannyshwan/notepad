'''
Replace all spaces with "%20" in a string given a string and the true length of the string
'''

def URLify(str, length):
    modifyStr = str[0:length]
    modifyStr = modifyStr.replace(" ", "%20")

    return modifyStr

string = "Mr John Smith      "
print(URLify(string, 13)) #Should print "Mr%20John%20Smith"