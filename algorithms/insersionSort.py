import time
from colors import *

def insertionSort(data, drawData, timer):
    for i in range(len(data)):
        temp = data[i]
        k = i
        while k > 0 and temp < data[k-1]:
            data[k] = data[k-1]
            k -= 1
        data[k] = temp
        drawData(data, [RED if x == k or x == i else MODERN for x in range(len(data))])
        time.sleep(timer)
        
    drawData(data, [MODERN for x in range(len(data))])