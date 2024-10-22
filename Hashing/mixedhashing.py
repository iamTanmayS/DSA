def hashing(n,a):
    chre = "".join(char  for char in n if char.isalnum())
    x = [0]*256
    for i in range(len(chre)):
        x[ord(chre[i])]+=1
    return x[ord(a)]
        
st = input("enter the alphabet")
print(f"Number of times {st} appears is {hashing("allo  , chalu cccccc232 hello ",st)}")

