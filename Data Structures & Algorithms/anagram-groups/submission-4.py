class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Input: strs = ["act","pots","tops","cat","stop","hat"]
        #.               
        #Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(word)
        return list(res.values())

            