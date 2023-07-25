class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()
        numsLen = len(nums)
        return(nums[numsLen//2])