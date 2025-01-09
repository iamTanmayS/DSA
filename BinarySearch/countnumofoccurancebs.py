def count(arr, x):
        def starin(arr,x):
            s = 0 
            e = len(arr)-1
            pos = -1
            while(s<=e):
                mid = (s+e)//2
                if x == arr[mid]:
                    pos = mid
                    e  = mid-1
                elif arr[mid]>x:
                    e = mid-1
                else:
                    s = mid+1
            return pos
        def endin(arr,x):
            
            s = 0 
            e = len(arr)-1
            pos = -1
            while(s<=e):
                mid = (s+e)//2
                if x == arr[mid]:
                    pos = mid
                    s  = mid+1
                elif arr[mid]>x:
                    e = mid-1
                else:
                    s = mid+1
                
            return pos
        
        a = starin(arr,x)
        b = endin(arr,x)
        
        if (b-a)!= 0:
            return (b-a)+1
        else:
            return 0
arr = [1, 1 ,2, 2 ,2 ,2 ,3]
x = 2
print(count(arr,x))