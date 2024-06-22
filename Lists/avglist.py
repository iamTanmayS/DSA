#Approach 1#

def avg(n):
    sum  = 0 
    for i in n:
        sum = sum+i
    return sum/len(n)


#Approach 2#

def avg2(n):
    return sum(n)/len(n)

x = [1,2,3,4,5,6,7,8,9,10]
print(avg2(x))