def mariuSort(arr):
    buckets = maxNumber(arr)
    #print(buckets)
    finished = []
    for i in range(len(arr)):
        buckets[arr[i]]+=1
    for i in range(len(buckets)):
        for j in range(buckets[i]):
            finished.append(i)
    return finished

def maxNumber(arr):
    l = 0
    n = []
    for i in range(len(arr)):
        if arr[i] > l: l = arr[i]
    for i in range(l+1):
        n.append(0)
    return n
