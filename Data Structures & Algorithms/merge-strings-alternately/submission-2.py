class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = min(len(word1), len(word2))
        res = ""
        while l < r:
            res += word1[l]
            res += word2[l]
            l += 1
        if l == len(word1) and l < len(word2):
            res+= word2[l:]
            print("word2 is longer")
        if l == len(word2) and l < len(word1):
            res+=word1[l:]
            print("word1 is longer") 
        return res
        