class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_count = Counter(t)
        window = defaultdict(int)

        have = 0
        need = len(t_count)
        left = 0

        res = [float("inf"), 0, 0]

        for right, char in enumerate(s):
            window[char] += 1
            if char in t_count and window[char] == t_count[char]:
                have += 1

            while have == need:
                current_len = right - left + 1

                if current_len < res[0]:
                    res = [current_len, left, right]

                left_char = s[left]
                window[left_char] -= 1
                if left_char in t_count and window[left_char] < t_count[left_char]:
                    have -= 1

                left += 1

        min_len, start, end = res
        return s[start : end + 1] if min_len != float("inf") else ""
