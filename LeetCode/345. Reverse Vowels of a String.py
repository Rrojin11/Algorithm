
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        tmp = [v for v in s if v in vowels]

        answer = ''

        for v in s:
            if v in vowels:
                answer+=(tmp.pop())
            else:
                answer+=v

        
        return answer
