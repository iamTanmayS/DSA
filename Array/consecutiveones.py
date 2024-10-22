def findMaxConsecutiveOnes(nums):
    count1 = 0
    count2 = 0
    for i in nums:
        if i == 1:
            count1+=1
        elif i ==0 :
            if count1>count2:
                count2 = count1
            count1 = 0
    if count1>count2:
        count2 = count1
    return count2


print(findMaxConsecutiveOnes([1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1]))