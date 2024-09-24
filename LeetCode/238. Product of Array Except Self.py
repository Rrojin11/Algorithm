class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #ver1.
        prod = 1
        idx_zero = []
        for i,v in enumerate(nums):
            if v!=0:
                prod *= v
            else:
                idx_zero.append(i)

        if not idx_zero:
            answer = []
            for v in nums:
                answer.append(prod//v)
        elif len(idx_zero)==1:
            answer = [0]*len(nums)
            answer[idx_zero[0]] = prod
        else:
            answer = [0]*len(nums)
        return answer

        #ver2.
        res = [1]
        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            res.append(prefix)
        
        postfix = 1
        for i in range(len(nums)-2,-1,-1):
            postfix *= nums[i+1]
            res[i] *= postfix
        return res
