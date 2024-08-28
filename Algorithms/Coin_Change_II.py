def change(self, amount: int, coins: List[int]) -> int:
        '''
        https://leetcode.com/problems/coin-change-ii/description/
        '''
        combinations=[0 for _ in range(amount+1)]
        combinations[0] = 1

        for coin in coins:
            for amt in range(1,amount+1):
                if amt >= coin:
                    combinations[amt]+= combinations[amt - coin]

        return combinations[amount] 