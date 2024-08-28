def repeatedCharacter(self, s: str) -> str:
        '''
        https://leetcode.com/problems/first-letter-to-appear-twice/description/
        '''
        hash_map={}
        for ch in s:
            if ch in hash_map.keys():
                if hash_map[ch]+1 == 2:
                    return ch
            else:
                hash_map[ch]=1
        return ''