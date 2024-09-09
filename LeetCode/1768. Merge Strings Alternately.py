class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lenWord1 = len(word1)
        lenWord2 = len(word2)
        minLen = min(lenWord1, lenWord2)
        answer = ""
        for i in range(minLen):
            answer+=(word1[i]+word2[i])
        
        if minLen == lenWord2: answer +=word1[minLen:]
        else: answer+=word2[minLen:]

        return answer
        
