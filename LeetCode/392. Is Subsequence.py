class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tmp = 0
        if len(s)==0:
            return True
        for i in t:
            if i==s[tmp]:
                tmp+=1
            if tmp==len(s):
                return True
        return False
        
