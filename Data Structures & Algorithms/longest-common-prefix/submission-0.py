class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word):
                    return answer
                if word[i] != strs[0][i]:
                    return answer
            answer += strs[0][i]
        return answer

        