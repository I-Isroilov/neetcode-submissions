class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        seen = set()
        best = 0

        while right < n:
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                best = max(best, right - left)
            else:
                seen.remove(s[left])
                left += 1
        return best
        