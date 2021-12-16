def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    l = []
    r = []
    for i in range(len(arr)):
        if i < len(arr)/2:
            l.append(arr[i])
        else: r.append(arr[i])
    l = mergeSort(l)
    r = mergeSort(r)
    return merge(l,r)

def merge(l,r):
    m = []
    while len(l) > 0 and len(r) > 0: 
        if(l[0] <= r[0]):
            m.append(l[0])
            l.pop(0)
        else:
            m.append(r[0])
            r.pop(0)
            
    while len(l) > 0:
         m.append(l[0])
         l.pop(0)

    while len(r) > 0:
         m.append(r[0])
         r.pop(0)
    return m

