''' def prime(a):
    
    count = 0
    for i in range(2,a):
        if (a % i == 0):
            count = count + 1
        
    if count == 0:
        return True
    else:
        return  False
    
    
def sieve(n):
    for i in range(1,n+1):
        if prime(i):
            print(i,end = " ")
            
n = int(input("enter the number: "))
sieve(n) '''


def sieve_of_eratosthenes(n):

  
  is_prime = [True] * (n + 1)
  is_prime[0] = False 
  is_prime[1] = False
  
  for p in range(2, int(n**0.5) + 1):

    if is_prime[p]:
      for i in range(p * p, n + 1, p):
        is_prime[i] = False

  return [i for i,isPrime in enumerate(is_prime) if isPrime]

n = int(input("enter the number: "))
primes = sieve_of_eratosthenes(n)
print("Prime numbers less than or equal to", n, ":", primes)
