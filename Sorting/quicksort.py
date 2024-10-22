def partitionindex(arr, low, high):
    pivot = arr[low]  
    i = low + 1
    j = high
    
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    
    arr[low], arr[j] = arr[j], arr[low]
    
    return j  

def quick(arr, low, high):
    if low < high:
        pivot_index = partitionindex(arr, low, high)
        quick(arr, low, pivot_index - 1)
        quick(arr, pivot_index + 1, high)


arr = [4,1,2,3,5]


quick(arr, 0, len(arr) - 1)

print(arr)