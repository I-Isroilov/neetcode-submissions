class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sortedNums = sorted(set(nums))
        count = 1
        longest = 1

        for i in range(1, len(sortedNums)):
            if sortedNums[i] == sortedNums[i -1] + 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 1
        return longest