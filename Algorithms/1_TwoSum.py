def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Link: https://leetcode.com/problems/two-sum/
        '''
        hash_map = {}
        nums_length = len(nums)
        for i in range(nums_length):
            potential_match = target - nums[i]
            if potential_match in hash_map.keys():
                return [hash_map[potential_match], i]
            else:
                hash_map[nums[i]] = i
        return []