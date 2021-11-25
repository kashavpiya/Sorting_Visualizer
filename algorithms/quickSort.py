import time
from colors import*

def partition(arr, low, high, drawData, timer):
    pivot = arr[high]
    j = low - 1
    for i in range (low, high):
        if arr[i] < pivot:
            j = j+1
            arr[j], arr[i] = arr[i], arr[j]
            
    arr[j+1], arr[high] = arr[high], arr[j+1]
    return (j+1)

def quickSort(arr, low, high, drawData, timer):
    if low < high:
        pi = partition(arr, low, high, drawData, timer)
        quickSort(arr, low, pi -1, drawData, timer)
        quickSort(arr, pi + 1, high, drawData, timer)

        drawData(arr, [RED if x >= low and x < pi else YELLOW if x == pi else DARK_BLUE if x > pi and x<= high else MODERN for x in range(len(arr)) ])

        time.sleep(timer)

    drawData(arr, [MODERN for x in range(len(arr))])        