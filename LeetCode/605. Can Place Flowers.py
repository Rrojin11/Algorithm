class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            now = flowerbed[i]
            leftC, rightC = False, False
            if now==0: #empty
                if i==0 or (flowerbed[i-1]==0):
                    leftC = True
                if i==(len(flowerbed)-1) or (flowerbed[i+1]==0): 
                    rightC = True
            print(i, leftC, rightC)
            if leftC and rightC:

                n-=1
                flowerbed[i]=1
        
        if n<=0: return True
        else: return False
            
