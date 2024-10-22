def sum(arr,x):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+ arr[j] == x:
                return i,j
    

print(sum([3,2,4],6))
            