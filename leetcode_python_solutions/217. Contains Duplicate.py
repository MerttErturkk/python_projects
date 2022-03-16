class Solution:
    def containsDuplicate(self, nums: List[int]):
        return len(nums) != len(set(nums))