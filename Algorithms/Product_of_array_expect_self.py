def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        https://leetcode.com/problems/product-of-array-except-self/
        '''
        result = [1 for _ in range(len(nums))]

        prefix = 1
        for i in range(len(nums)):
            result[i]=prefix
            prefix*=nums[i]
            
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=postfix
            postfix*=nums[i]

        return result