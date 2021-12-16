import matplotlib.pyplot as plt

from get_time import *
from Array_Generator import *
from _bubbleSort import *
from _selectionSort import *
from _mergeSort import *
from _quickSort import *
from _quick3 import *
from _mariuSort import *

algos = [mariuSort,quickSort,mergeSort,bubbleSort,quick3,selectionSort]

def master(n,arrType,algoAmount):

    data = [
        [],
        [],
        [],
        [],
        [],
        []
    ]

    dataY = [
        [],
        [],
        [],
        [],
        [],
        []
    ]
    
    for i in range(len(algos)-(6-algoAmount)):
        for j in range(1,n+1):
            data[i].append(getTime(algos[i],1000*j,arrType))
            print(algos[i],1000*j)
            dataY[i].append(1000*j)
    if algoAmount >= 1: plt.plot(dataY[0], data[0], label = "MariuSort")
    if algoAmount >= 2: plt.plot(dataY[0], data[1], label = "QuickSort")
    if algoAmount >= 3: plt.plot(dataY[0], data[2], label = "MergeSort")
    if algoAmount >= 4: plt.plot(dataY[0], data[3], label = "Bubblesort")
    if algoAmount >= 5: plt.plot(dataY[0], data[4], label = "Quick3")
    if algoAmount >= 6: plt.plot(dataY[0], data[5], label = "Selectionsort")


    plt.legend()
    plt.xlabel('Size of n')
    plt.ylabel('Time in seconds')
    plt.title(arrType) 
    plt.show()


master(50,'sorted',4)
