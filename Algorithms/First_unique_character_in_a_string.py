def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for ch in s:
            if ch in hash_map.keys():
                hash_map[ch]+=1
            else:
                hash_map[ch]=1
        
        for k,v in hash_map.items():
            if v==1:
                return s.index(k)
        return -1