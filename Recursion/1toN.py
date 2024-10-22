def printn(n):
    if n == 0: 
        return
    printn(n-1)
    print(n)
    
    
    
printn(10)
