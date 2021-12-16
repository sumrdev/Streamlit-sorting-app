from math import e
import sys

sys.setrecursionlimit(999999)
def quickSort(s):
    if len(s) <= 1: return s
        
    pivot = s[len(s)//2]
    g = []
    l = []
    
    for i in range(1, len(s)):
        if s[i] >= pivot: g.append(s[i])
        else: l.append(s[i])
    return quickSort(l) + [pivot] + quickSort(g)
