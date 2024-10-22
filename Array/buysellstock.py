def buysellbrute(prices):
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]>prices[i]:
                    x = prices[j]-prices[i]
                    if profit<x:
                        profit = x 
        
        return profit

def buysellbetter(prices):
        profit = 0
        for i in range(len(prices)):
            li = prices[0:i+1]
            minl = prices[i]
            if len(li)>0:
                minl = min(li)
            x = prices[i]-minl
            if profit < x:
                profit = x
        return profit
    
def buyselloptimized(prices):
        minl = prices[0]
        profit = 0
        for i in range(len(prices)):
            cost = prices[i]-minl
            profit = max(profit,cost)
            minl = min(minl,prices[i])
        
        return profit
    

print(buysellbrute([7,6,4,3,1]))
print(buysellbetter([7,6,4,3,1]))
print(buyselloptimized([7,6,4,3,1]))