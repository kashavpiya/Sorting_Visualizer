def heapify(arr, n, i):
    maximum = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[maximum] > arr[left]:
        maximum = left
        
    if right < n and arr[maximum] > arr[right]:
        maximum = right
        
    if maximum != i:
        arr[maximum], arr[i] = arr[i], arr[maximum]
        heapify(arr, n, maximum)
        
def heapSort(arr):
    n = len(arr)
    for i in range (n//2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range (n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i]),