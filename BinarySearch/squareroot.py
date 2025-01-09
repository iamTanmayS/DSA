def floorSqrt(n): 
        i = 1
        count = 0
        while(n>=0):
            n = n-i
            count+=1
            i+=2
        return count
    
    
print(floorSqrt(5))