import time
from colors import*

def bubbleSort(arr,  drawData, timer):
    n = len(arr)
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                drawData(arr, [RED if x==j or x== j +1 else MODERN for x in range (len(arr))])
                time.sleep(timer)
    drawData(arr, [MODERN for x in range(len(arr))])  
        
    