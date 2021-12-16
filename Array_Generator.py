import random

def genArr(iterations,arrType):
    if arrType == 'Random':
        return randomArr(iterations)
    elif arrType == 'Reverse Order':
        return reverseArr(iterations)
    elif arrType == 'Few Uniques':
        return fewUniqueArr(iterations)
    elif arrType == 'Nearly Sorted':
        return nearlySortedArr(iterations)
    elif arrType == 'Sorted':
        return sorted(iterations)

def randomArr(iterations):
    arr = []
    for i in range(iterations):
        arr.append(random.randint(0,10000000))
    return arr

def reverseArr(iterations):
    arr = []
    for i in range(iterations,0,-1):
        arr.append(i)
    return arr

def fewUniqueArr(iterations):
    arr = []
    for i in range(iterations):
        arr.append(random.randint(0,100))
    return arr

def sorted(iterations):
    arr = []
    for i in range(iterations):
        arr.append(i)
    return arr


def nearlySortedArr(iterations):
    arr = []
    for i in range(iterations):
        x = random.randint(0,9)
        if x == 0:
            arr.append(random.randint(0,iterations))
        else: arr.append(i)
    return arr
