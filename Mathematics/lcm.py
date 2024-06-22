

#Approach 1#
def lcm():
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the Second number: "))
    
    a = max(num1, num2)
    temp = a 
    while(True):
        if(a%num1 == 0 and a%num2 == 0):
            print(f"Lcm of {num1} and {num2} is {a}")
            break
        else:
            a = a+temp
            
            
lcm()