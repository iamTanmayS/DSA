def hashing(x,n):
    dicto = {}
    chare = "".join(charo for charo in x if charo.isalnum())
    for i in chare:
        if i in dicto:
            dicto[i] += 1
        else:
            dicto[i] = 1
    if n not in dicto:
        return dicto.get(n, 0) 
    return dicto[n]
    


print(hashing("hello  wordld dd","d"))