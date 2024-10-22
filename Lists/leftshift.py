def deleteFromArray(arr,n,idx):

    for i in range(idx+1,n):
            arr[i-1] = arr[i]
    arr.pop()
    return arr



arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)

idx = 4

print(deleteFromArray(arr,n,idx))