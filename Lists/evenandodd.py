def fun(n):
    even = []
    odd = []
    for i in n :
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

x = [1,2,9,10,13,14,15,3,4,5,6,7,8,16,11,12]
even,odd = fun(x)
print("even list : ",even)
print("odd list : ",odd)