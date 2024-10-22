def selection(n):
    for i in range(len(n)):
        min = i
        for j in range(i+1, len(n)):
            if n[j] < n[min]:
                min = j
        temp = n[i]
        n[i] =  n[min]
        n[min] = temp
    return n


print(selection([1,21,32,1,2,1,2,1,23,4,5,7,5,4,3,276]))
