def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''
        https://leetcode.com/problems/minimum-cost-for-tickets
        '''
        min_cost = [0 for _ in range(366)]
        min_cost[0] = 0
        last_day = days[-1]
        for i in range(1,last_day+1):
            if i in days:
                one_day_cost = min_cost[max(0,i-1)]+costs[0]
                seven_day_cost = min_cost[max(0,i-7)]+costs[1]
                thirty_day_cost = min_cost[max(0,i-30)]+costs[2]
                min_cost[i] = min(one_day_cost,seven_day_cost,thirty_day_cost)
            else:
                min_cost[i] = min_cost[i-1]
        return min_cost[last_day]