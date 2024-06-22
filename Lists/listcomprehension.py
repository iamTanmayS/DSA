l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y = int(input("enter the number : "))
print("Less than ",y,":",[x for x in l1 if x<y]) 
print("even terms : ",[x for x in l1 if x%2 == 0 ])
print("odd terms : ",[x for x in l1 if x%2 != 0 ])