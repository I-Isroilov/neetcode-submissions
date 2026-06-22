class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current_subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(current_subset.copy())
                return

            current_subset.append(nums[i])
            backtrack(i + 1)

            current_subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
        