def prime(a):
    count = 0
    for i in range(2,a):
        if (a % i == 0):
            count = count + 1
        
    if count == 0:
        return True
    else:
        return  False


def primefactorization(g):
    for i in range(2,g+1):
       if prime(i) : 
           x = i 
           while(g % x == 0):
               print(i,end = "*")
               x = x*i
               
n = int(input("enter the number : "))      
primefactorization(n)
 
 
 