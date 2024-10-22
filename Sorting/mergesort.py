        
        
def merge(arr,low,mid,high):        
    temp = []
    left = low
    right= mid+1
    while(left<=mid and right<=high):
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=high):
        temp.append(arr[right])
        right+=1
    for i in range(len(temp)):
        arr[low+i] = temp[i]
        


def mergesort(arr,low,high):
    mid=(low+high)//2
    if (high<=low):
        return
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr,low,mid,high)
    
    
arr =  [98,43,2,54,7,111,211,2,1,5,6] 
mergesort(arr,0,len(arr)-1)
print(arr)
