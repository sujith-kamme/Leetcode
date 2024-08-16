def isSubsequence(self, s: str, t: str) -> bool:
        '''
        https://leetcode.com/problems/is-subsequence/
        '''
        if len(s) == 0:
            return True
        
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j +=1
            if j == len(s):
                return True
        return False