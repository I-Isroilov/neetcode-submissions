class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length

        prefix = 1
        for i in range(length):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(length - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

        
