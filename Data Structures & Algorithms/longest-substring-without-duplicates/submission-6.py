class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #s = "zxyzxyz"
        #.     l r 
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            res = max(res, len(s[l:r]) +1)
        return res
            

        