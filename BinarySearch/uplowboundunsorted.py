def getFloorAndCeil(x,arr):
        f = -1
        c = -1
        for i in arr:
            if i<= x:
                f = max(f,i)
            if i>= x:
                if c == -1 or i < c:
                    c = i
        return f,c
                
                

    
    
x = 7 
arr = [5, 6, 8, 9, 6, 5, 5, 6]
print(getFloorAndCeil(x,arr))

