class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cfreq_per_word = defaultdict(list)
        #((1A, 2B, 3C):[words, words, words])
        for s in strs:
            word = [0] * 26
            for c in s:
                word[ord(c) - ord('a')] += 1
            cfreq_per_word[tuple(word)].append(s)
        return list(cfreq_per_word.values())
