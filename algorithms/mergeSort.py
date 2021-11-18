import time
from colors import *

def merge(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1

def mergeSort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)

        #divide the first half
        mergeSort(data, start, mid, drawData, timeTick)

        #divide the second half
        mergeSort(data, mid+1, end, drawData, timeTick)

        #doing the comparison and combining (conquer)
        merge(data, start, mid, end, drawData, timeTick)

        drawData(data, [RED if x >= start and x < mid else YELLOW if x == mid 
                        else BLUE if x > mid and x <=end else MODERN for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [MODERN for x in range(len(data))])

