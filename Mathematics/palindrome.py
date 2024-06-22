number = input("enter the numeber: ")

#Approach 1 #
"""

temp = number
reverse = 0 
while temp > 0:
    dig = temp%10
    reverse = (reverse*10)+dig
    temp = temp//10
if number == reverse:
    print("palindrome")
else:
    print("not a palindrome") 


"""

#Approach 2 #
"""

reverse = number[::-1]
if number == reverse:
    print("palindrome")
else:
    print("not a palindrome")

"""