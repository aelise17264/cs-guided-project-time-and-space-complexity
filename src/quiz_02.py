def csFindAddedLetter(str_1, str_2):
    smallStr = ""
    bigStr = ""

    if(len(str_1) > len(str_2)):
        smallStr = str_2
        bigStr = str_1
    else:
        smallStr = str_1
        bigStr = str_2
    smallStrCodeTotal = 0
    bigStrCodeTotal = 0
    i = 0
      
    # Add Character codes of both the strings 
    while(i < len(smallStr)): 
        smallStrCodeTotal += ord(smallStr[i]) 
        bigStrCodeTotal += ord(bigStr[i]) 
        i += 1
      
    bigStrCodeTotal += ord(bigStr[i]) 
 
    intChar = bigStrCodeTotal - smallStrCodeTotal 
    return chr(intChar)
    
print (csFindAddedLetter("bf", "bfb" ))
print (csFindAddedLetter("bcde", "bcdef"))
print (csFindAddedLetter("xqmxtheyvpdqounqmfyaqdqxwe", "xqmxtheyvpdqounqmfyaqxdqxwe"))