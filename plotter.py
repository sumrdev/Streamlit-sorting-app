import matplotlib.pyplot as plt
from Array_Generator import *
from get_time import *
from Array_Generator import *
from _bubbleSort import *
from _selectionSort import *
from _mergeSort import *
from _quickSort import *
from _quick3 import *
from _mariuSort import *



def master(ntemp,arrType,usedAlgos):
    fig, ax = plt.subplots()
    algos = [mariuSort,quickSort,mergeSort,bubbleSort,quick3,selectionSort]
    chosenString = usedAlgos
    chosen = methodConvert(usedAlgos)

    data = {
        'Mariusort': [],
        'Quicksort': [],
        'Mergesort': [],
        'Bubblesort': [],
        'Quick3': [],
        'Selectionsort': []
    }

    dataY = {
        'Mariusort': [],
        'Quicksort': [],
        'Mergesort': [],
        'Bubblesort': [],
        'Quick3': [],
        'Selectionsort': []
    }


    n = ntemp
    step = int(n/10)
    for a,x in zip(chosen,chosenString):
        for j in range(1,11):
            data[x].append(getTime(a,j*step,arrType))
            dataY[x].append(j*step)
    if 'Mariusort'      in usedAlgos: ax.plot(dataY['Mariusort'], data['Mariusort'], label = "MariuSort")
    if 'Quicksort'      in usedAlgos: ax.plot(dataY['Quicksort'], data['Quicksort'], label = "QuickSort")
    if 'Mergesort'      in usedAlgos: ax.plot(dataY['Mergesort'], data['Mergesort'], label = "MergeSort")
    if 'Bubblesort'     in usedAlgos: ax.plot(dataY['Bubblesort'], data['Bubblesort'], label = "Bubblesort")
    if 'Quick3'         in usedAlgos: ax.plot(dataY['Quick3' ], data['Quick3' ], label = "Quick3")
    if 'Selectionsort'  in usedAlgos: ax.plot(dataY['Selectionsort'], data['Selectionsort'], label = "Selectionsort")


    ax.legend()
    ax.set_xlabel('Size of n')
    ax.set_ylabel('Time in seconds')
    ax.set_title(arrType) 
    print('returning plot with specs',n,arrType,usedAlgos)
    return fig

def methodConvert(usedAlgos):
    methods = []
    if 'Bubblesort' in usedAlgos: methods.append(bubbleSort)
    if 'Mergesort' in usedAlgos: methods.append(mergeSort)
    if 'Quicksort' in usedAlgos: methods.append(quickSort)
    if 'Quick3' in usedAlgos: methods.append(quick3)
    if 'Mariusort' in usedAlgos: methods.append(mariuSort)
    if 'Selectionsort' in usedAlgos: methods.append(selectionSort)
    return methods

def stringConvert(chosen):
    methods = []
    if bubbleSort in chosen: methods.append('Bubblesort')
    if mergeSort in chosen: methods.append('Mergesort')
    if quickSort in chosen: methods.append('Quicksort')
    if quick3 in chosen: methods.append('Quick3')
    if mariuSort in chosen: methods.append('Mariusort')
    if selectionSort in chosen: methods.append('Selectionsort')
    return methods

def getIndex(a,n):
    print(a)
    data = ['Mariusort', 'Quicksort', 'Mergesort', 'Bubblesort', 'Quick3', 'Selectionsort']
    for i in range(n):
        if a == data: print(i)
