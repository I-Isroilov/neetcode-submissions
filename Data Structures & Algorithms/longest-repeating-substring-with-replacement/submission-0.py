class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0]*26
        left = 0
        max_count = 0
        best = 0

        for right in range(n):
            idx_r = ord(s[right]) - 65
            freq[idx_r] += 1

            if freq[idx_r] > max_count:
                max_count = freq[idx_r]

            while (right - left + 1) - max_count > k:
                idx_l = ord(s[left]) - 65
                freq[idx_l] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best       