def bubbleSort(l):
    n = len(l)
    for i in range(n-1):
        a = True
        for j in range(0,n-i-1):
            if(l[j] > l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
                a = False
        if a: return l
    return l
