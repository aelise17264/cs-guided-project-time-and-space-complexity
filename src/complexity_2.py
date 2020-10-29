def removeDuplicate(arr):
    differents = {}
    for i in arr:
        if i not in differents:
            differents[i] = []
        differents[i] += [i]

    return differents.keys()

print(removeDuplicate([1,1,2,4,5,5,3,3,1,2]))

