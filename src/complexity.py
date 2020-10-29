#we only multiply when some logic is nested
#when code is stacked sequentially on top of one another we add their respective runtimes

#O(1) + O(1)+ O(1)+ O(0.5n) + O(2000)
#O(1 + 1 + 1+ 0.5n + 2000)
#O(n + 2003)
#O(n)

def do_something(items):
    last_idx = len(items) -1 #getting the length is O(1)

    print(items[last_idx]) #accessing an array element via index - O(1)
                            #we'll consider printing/console logging O(1)

    middle_idx = len(items) / 2 #arithmetic operations - O(1)
    idx = 0                     # initializing a variable - O(1)
    

    while idx < middle_idx: # this loop only runs over half our items -> 0.5 * n
        print(items[idx]) 
        idx = idx + 1
    
    # for num in range (2000): # this has nothing to do w/ the length of our list -> O(2000)
    #     print(num)            #O(1)

print(do_something([1, 2, 3, 4]))