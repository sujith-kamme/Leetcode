def findTheDifference(self, s: str, t: str) -> str:
        '''
        https://leetcode.com/problems/find-the-difference/
        '''
        s_set = set(s)
        t_set = set(t)
    
        difference= t_set.difference(s_set)
        return ''.join(difference)