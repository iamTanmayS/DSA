#Approach 1#

def fun(x):
    res = x[0]
    for i in x :
        for j in x:
            if i>j:
                res = i
    return res


#Approach 2#

def fun2(x):
    res = x[0]
    for i in x : 
        if i > res:
            res = i
            
    return res





