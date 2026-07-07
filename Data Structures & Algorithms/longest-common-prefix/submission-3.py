class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        for i in range(len(strs[0])): #i is going to go up to the lenght of the first string
            for word in strs:
                if len(word) == i or word[i] != strs[0][i]:
                    return answer
            answer += strs[0][i]
        return answer
        