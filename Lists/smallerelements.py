def fun(x,n):
    newlist = []
    for i in n:
        if i < x :
            newlist.append(i)
    return newlist


x = int(input("enter the number: "))

n = [1,2,3,4,5,6,7,8,9,10]

print(fun(x,n))
            
    