def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        https://leetcode.com/problems/coin-change/
        '''
        min_coins = [float('inf') for _ in range(amount+1)]
        min_coins[0]=0
        for coin in coins:
            for amt in range(1,amount+1):
                if coin <= amt:
                    min_coins[amt] = min(min_coins[amt], min_coins[amt - coin] + 1)
        
        return min_coins[-1] if min_coins[-1]!= float('inf') else -1