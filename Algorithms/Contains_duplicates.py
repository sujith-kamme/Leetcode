def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        https://leetcode.com/problems/contains-duplicate/
        '''
        return len(nums)-len(set(nums))!=0