def insertion(x):
    for i in range(1,len(x)):
        s = x[i]
        j = i-1
        while j>=0 and x[j]>s:
            x[j+1] = x[j] 
            j-=1
        x[j+1] = s
    return x


print(insertion([1,21,32,1,2,1,2,1,23,4,5,7,5,4,3,276]))
            
    