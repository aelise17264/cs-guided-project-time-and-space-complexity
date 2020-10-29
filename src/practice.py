def addTwoDigits(n):
    intiger = 0
    for digit in str(n):
        intiger += int(digit)
    return int(intiger)
print(addTwoDigits(29))