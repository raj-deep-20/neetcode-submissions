class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] != i:
                return i
        return n'''
        num_set = set(nums)
        n = len(nums)
        for i in range(n+1):
            if i not in num_set:
                return i