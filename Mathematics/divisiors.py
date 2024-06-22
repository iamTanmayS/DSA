n = int(input("enter the number"))
def divisors(a):
     for i in range(1,a+1):
          if a%i == 0:
               print(i)

divisors(n)