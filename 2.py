def getCase(word):
    
    if word.isupper():
        return "upper"
    
    elif word.islower():
        return "lower"
    
    else:
        return "mixed"


print(getCase("whisper...")) 
print(getCase("SHOUT!")) 
