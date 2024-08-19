def findTheDifference(self, s: str, t: str) -> str:
        '''
        https://leetcode.com/problems/find-the-difference/
        '''
        xor = 0
        for ch in t:
            xor^=ord(ch)
        for ch in s:
            xor^=ord(ch)
        
        return chr(xor)