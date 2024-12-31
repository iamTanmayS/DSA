class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = 365
        travel_days = set(days)
        dp = [0] * (max_day + 1)

        for i in range(1, max_day + 1):
            if i not in travel_days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0], 
                    dp[max(0, i - 7)] + costs[1],  
                    dp[max(0, i - 30)] + costs[2]  
                )
        
        return dp[max_day]
