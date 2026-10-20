class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        schars = [0 for num in range(0,25)]
        tchars = [0 for num in range(0,25)]
        for c in s:
            schars[ord('a') - ord(c)] +=1
        for p in t:
            tchars[ord('a') - ord(p)] +=1
        if schars == tchars:
            return True
        else:
            return False

 
        