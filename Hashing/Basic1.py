def hashing(n,g):
    x = [0 for i in range(22)]
    for i in range(len(n)):
            x[n[i]]+=1
            
    return x[g]


print(hashing([1,2,3,4,5,6,7,3,5,21,7,4,5],7))




    