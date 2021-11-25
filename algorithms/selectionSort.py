import time
from colors import *

def selectionSort(data, drawData, timer):
    for i in range(len(data)-1):
        min = i
        for k in range(i+1, len(data)):
            if data[k] < data[min]:
                min = k

        data[min], data[i] = data[i], data[min]
        drawData(data, [RED if x == min or x == i else MODERN for x in range(len(data))] )
        time.sleep(timer)
        
    drawData(data, [MODERN for x in range(len(data))])