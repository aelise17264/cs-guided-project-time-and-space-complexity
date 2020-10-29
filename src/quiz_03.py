def csFirstUniqueChar(input_str):
    frequency = {}

    for i in input_str:
        if i not in frequency:
            frequency[i] = 1
            
        else:
            frequency[i] += 1
            
    for i in range(len(input_str)):
        if frequency[input_str[i]] == 1:
            return i
    return -1 

       
print(csFirstUniqueChar("lambda"))
print(csFirstUniqueChar("lambdaschool"))
print(csFirstUniqueChar("ilovelambdaschool"))
print(csFirstUniqueChar("vvv"))
    