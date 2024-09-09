class Solution:
    def getPrefix(self,tmp):
        n = len(tmp)
        prefixs = []
        for i in range(1,n//2+1):
            if n%i==0:
                if tmp[:i]*(n//i)==tmp:
                    prefixs.append(tmp[:i])
        prefixs.append(tmp)
        return prefixs
            
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        p1 = self.getPrefix(str1)
        p2 = self.getPrefix(str2)
        

        answer = ""
        if len(str1)>len(str2):
            for i in p2:
                if i in p1:
                    answer = i
        else:
            for i in p1:
                if i in p2:
                    answer = i
        return answer

        


        
