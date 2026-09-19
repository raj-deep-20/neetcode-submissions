class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map={}
        for i, num in enumerate(nums):
            complement = target - nums[i]
            if complement in freq_map:
                return [freq_map[complement],i]
            freq_map[num] = i