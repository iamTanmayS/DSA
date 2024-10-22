
def printn(f,n,x):
    if (n>=x/2):
        return 
    swap(f,n,x-n-1)
    printn(f,n+1,x)
    return f
    
def swap(f,n,x):
    temp = f[n]
    f[n] = f[x]
    f[x] = temp     
    
f  = [1,2,3,4,5,6,7,8,9,10,11] 
print(printn(f,0,len(f)))