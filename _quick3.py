from Array_Generator import *
import sys

sys.setrecursionlimit(999999)

def quick3(arr):
    if(len(arr) <=1): return arr

    left = arr[0]
    right = arr.pop()
    if left > right: left, right = right, left

    l = []
    m = []
    h = []

    for i in range(1, len(arr)):
        if arr[i] <= left: l.append(arr[i])
        elif arr[i] >= right: h.append(arr[i])
        elif arr[i] >= left and arr[i] < right: m.append(arr[i])
    return quick3(l) + [left] + quick3(m) + [right] + quick3(h)