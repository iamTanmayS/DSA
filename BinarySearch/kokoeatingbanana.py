import math


#Brute Force
def minEatingSpeed(piles,h):
        speed = max(piles)
        for i in range(1,max(piles)+1):
            sum = 0
            for j in piles:
                sum += math.ceil(j / i)
            if sum<= h: 
                speed = min(speed,i)
        return speed
    


#Optimized approach using binary search
def binaryMinEatingSpeed(piles,h):
        l = 1
        high = max(piles)
        while(l<=high):
            mid = (l+high)//2
            sum = 0
            for pile in piles:
                sum += math.ceil(pile/mid)
            if sum<=h:
                result = mid
                high = mid-1
            else:
                l = mid+1
        return result
    
    
piles = [3,6,7,11]
h = 8
print(binaryMinEatingSpeed(piles,h))