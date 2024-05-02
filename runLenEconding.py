# Encoded Data
def encodeString(stringVal):
    encodedData =[]
    prevChar =stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != char:
            encodedData.append((prevChar,count))
            count =0
            prevChar=char
            count = count +1
    encodedData.append((prevChar,char))  
    return encodedData
        
# Decoded Data
def decodeString(encodedData):
    decodedData =''
    for item in encodedData:
     decodedData = decodedData +item[0] *item[1]
    return decodedData 

print(encodeString('AAAAABBBBCCC'))              
