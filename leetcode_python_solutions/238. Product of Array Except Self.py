class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from numpy import prod,array
        nums = array(nums)
        out=[]
        for i in range(len(nums)):
            prev, to_prod = nums[:i],nums[i+1:] 
            out.append(prod(to_prod)*prod(prev))
        return out
            
        