def firstBadVersion(self, n: int) -> int:
        '''
        https://leetcode.com/problems/first-bad-version/description/
        '''
        low = 0
        high = n
        version = 1
        while(low<=high):
            ptr = (low+high)//2
            if not isBadVersion(ptr):
                low = ptr + 1
            else:
                high = ptr-1
                version = ptr
        return version