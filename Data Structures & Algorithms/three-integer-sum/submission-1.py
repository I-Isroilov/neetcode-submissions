class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue

            left, right = i+1, n-1
            while left < right:
                s = sortedNums[i] + sortedNums[left] + sortedNums[right]

                if s == 0:
                    res.append([sortedNums[i],sortedNums[left], sortedNums[right]])

                    while left < right and sortedNums[left] == sortedNums[left+1]:
                        left += 1
                    while left < right and sortedNums[right] == sortedNums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return res

                    
        


        
        
        