class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      n, m = len(s1), len(s2)

      if n > m: return False

      s1_count, s2_count = [0] * 26, [0] * 26

      for i in range(n):
        s1_count[ord(s1[i]) - ord('a')] += 1
        s2_count[ord(s2[i]) - ord('a')] += 1

      matches = 0
      for i in range(26):
        if s1_count[i] == s2_count[i]:
            matches += 1

      for i in range(n, m):
        if matches == 26:
            return True

        index_in = ord(s2[i]) - ord('a')
        index_out = ord(s2[i - n]) - ord('a')

        s2_count[index_in] += 1
        if s2_count[index_in] == s1_count[index_in]:
            matches += 1
        elif s2_count[index_in] - 1 == s1_count[index_in]:
            matches -= 1

        s2_count[index_out] -= 1
        if s2_count[index_out] == s1_count[index_out]:
            matches += 1
        elif s2_count[index_out] + 1 == s1_count[index_out]:
            matches -= 1

      return matches == 26

        



        