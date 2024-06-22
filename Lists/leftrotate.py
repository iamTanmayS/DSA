def rotateleft(n):
    l = len(n)
    x = n[0]
    for i in range(1,l):
        n[i-1] = n[i]
    n[l-1] = x
    return n



n = [1,2,3,4,5,6,7,8]
print(rotateleft(n))