class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord("a")] += 1
            res[tuple(freq)].append(word) #right here we are making the key be the char freq array and the value is the word that made that char freq array
            #we do that for each word where the res hasmap is going to have arrays as keys and words as values
            #for each value of arrays that are identical, we add them to the same subarray in the same array 
        return list(res.values())