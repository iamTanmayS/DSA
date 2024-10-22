def lconoptimal(nums):
    cur = 0
    ls  = 0
    cs = 0
    numset = set(nums)
    for i in numset:
        if i-1 not in numset:
            cur = i
            cs = 1
        while cur+1 in numset:
            cs+=1
            cur = cur+1
        ls = max(cs,ls)
    return ls


print(lconoptimal([1,2,2,3,4,5,4,3,2,1,6,55,43,34,3,232,32,21,1,43,43]))            