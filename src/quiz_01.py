def csSortedTwoSum(numbers, target):
    dict = {}
    for i in range(len(numbers)):
        dict[numbers[i]] = i      
    for i in range(len(numbers)): 
        complement = target - numbers[i] 
        if complement in dict and dict[complement] != i: 
            return [i, dict[target - numbers[i]]] 

print (csSortedTwoSum([2,5,9,13], 7))
