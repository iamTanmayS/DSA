from largest import fun2

#Approach 1#
def seclargest(c):
    a = fun2(c)
    c.remove(a)
    return (fun2(c))
            
#Approach 2#

def seclargest2(c):
    lar = c[0]
    seclar = None
    for i in x: 
        if i > lar:
            seclar = lar
            lar = i
        elif i!=lar:
            if seclar == None or seclar < i:
                seclar = i
    return seclar
        

x = [1,9,5,2,3,4]
print(seclargest2(x))