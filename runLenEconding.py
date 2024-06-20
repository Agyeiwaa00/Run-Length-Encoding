# Encoded Data
def encodeString(stringVal):
    encodedData =[]
    prevChar =stringVal[0] # defining previous character
    count = 0
    for char in stringVal:
        if prevChar != char: # comparing previous character to current character
            encodedData.append((prevChar,count)) # add previous character to the count
            count = 0 # reset the count 
            prevChar=char
            count = count + 1
    encodedData.append((prevChar,char))  
    return encodedData
        
# Decoded Data
def decodeString(encodedData):
    decodedData =''
    for item in encodedData:
     decodedData = decodedData +item[0] *item[1]
    return decodedData 

print(encodeString('AAAAABBBBCCC')) 
            
