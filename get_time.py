from Array_Generator import *
import time

def getTime(algo,n,arrayType):
    a = genArr(n,arrayType)
    s = time.time()
    sorted = algo(a)
    e = time.time()
    return e-s