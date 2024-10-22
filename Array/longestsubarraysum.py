def long(arr,n,k):
    lon= []
    cur = []
    for i in range(len(arr)):
        sum = 0 
        for j in range(i,len(arr)):
            sum = sum+arr[j]
            if sum == k:
                cur = arr[i:j+1]
            if len(lon) < len(cur):
                lon = cur
    return len(lon)
            
        

            
        
      
print(long([1,1,2,5,6,5,3,1,1,1,2,3],3,5))
            