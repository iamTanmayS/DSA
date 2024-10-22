def singleNumber(nums):
        di = {}
        for i in nums:
            if i in di :
                di[i]+=1
            else :
                di[i]  = 1
        for i in di:
            if di[i]== 1:
                return i
        print(di)
nums=[-1]
print(singleNumber(nums))