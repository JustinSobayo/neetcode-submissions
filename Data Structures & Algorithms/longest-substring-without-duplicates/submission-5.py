class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #"pwwkew"
        #  i
        #  j
        #(w, )
        i = 0
        sub = set()
        res = 0
        for j in range(len(s)):
            while s[j] in sub:
                sub.remove(s[i])
                i += 1
            sub.add(s[j])
            res = max(res, j-i+1)
        return res