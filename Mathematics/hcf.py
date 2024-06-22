number1 = input("enter the numbers seprated by space : ")
number2 = int(input("enter the numbers seprated by space : "))


#Approach 1#
''' if number1 >= number2:
    while(number2 != 0):
        remainder = number1 % number2
        number1 = number2
        number2 = remainder
    print(number1)

elif number1 <= number2:
    while(number1 != 0):
        remainder = number2 % number1
        number2 = number1
        number1 = remainder
    print(number2) '''
    

#Approach 2#

''' hcf = 1 
a = min(number1, number2)
for i in range(1,a+1):
    if number1%i == 0 and number2%i == 0:
        hcf = hcf * i
print(hcf) '''