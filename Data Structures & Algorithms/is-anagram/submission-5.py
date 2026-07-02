class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #s = "carrace"
        #t = "racecar"
        s_frequency = {}
        t_frequency = {}
        for char in s:
            if char in s_frequency:
                s_frequency[char] += 1
            else:
                s_frequency[char] = 1
        for char in t:
            if char in t_frequency:
                t_frequency[char] += 1
            else:
                t_frequency[char] = 1
        if len(s_frequency) == len(t_frequency):
            for key,value in s_frequency.items():
                if key in t_frequency:
                    if s_frequency[key] == t_frequency[key]:
                        continue
                    else:
                        return False
                else:
                    return False
            return True
        else:
            return False

 
        