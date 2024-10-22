def hashing(x,n):
    dicto = {}
    for i in x:
        if i in dicto:
            dicto[i] += 1
        else:
            dicto[i] = 1
    return dicto[n]

x = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,4, 5]
# print(hashing(x,5))

