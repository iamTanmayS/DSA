def palindrone(n,i,x):
    if (i>=len(n)/2):
        return
    if (n[i] != n[x]):
        return False
    palindrone(n,i+1,x-i-1)
    return True   

a = "madaa"
print(palindrone(a,0,len(a)-1))



