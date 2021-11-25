import time
from colors import *

def heapify(arr, n, i, drawData, timer):
    maximum = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[maximum] > arr[left]:
        maximum = left
        
    if right < n and arr[maximum] > arr[right]:
        maximum = right
        
    if maximum != i:
        arr[maximum], arr[i] = arr[i], arr[maximum]
        heapify(arr, n, maximum, drawData, timer)
        
def heapSort(arr, drawData, timer):
    n = len(arr)
    for i in range (n//2 - 1, -1, -1):
        heapify(arr, n, i, drawData, timer)
        
    for i in range (n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, drawData, timer)

        drawData(arr, [YELLOW if x==i else MODERN for x in range(n)])
        time.sleep(timer)

    drawData(arr, [MODERN for x in range(len(arr))])
        
