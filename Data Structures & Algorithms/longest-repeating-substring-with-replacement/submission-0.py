class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #s = "XYYX", k = 2 
        #.    ij
        #s = "AAABAABB", k = 1
        #.    i  j
        chars = {}
        l = 0
        res = 0
        for r in range(len(s)):
            chars[s[r]] = 1 + chars.get(s[r], 0)
            while len(s[l:r]) + 1 - max(chars.values()) > k:
                chars[s[l]] -= 1
                l += 1
            res = max(res, len(s[l:r])+1)
        return res
