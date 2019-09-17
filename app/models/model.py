def flipit(string):
    newstring = ""
    for n in string:
        newstring = n + newstring
    return newstring

print(flipit("string"))

def shout(string):
    return string.upper()
print(shout("string"))
