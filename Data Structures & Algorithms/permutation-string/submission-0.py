class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len, s2Len = len(s1), len(s2)

        if s1Len > s2Len: return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(s1Len):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        for i in range(s1Len, s2Len):
            if matches == 26: return True

            index_in = ord(s2[i]) - ord('a')
            index_out = ord(s2[i - s1Len]) - ord('a')

            s2Count[index_in] += 1
            if s2Count[index_in] == s1Count[index_in]:
                matches += 1
            elif s2Count[index_in] - 1 == s1Count[index_in]:
                matches -= 1

            s2Count[index_out] -= 1
            if s2Count[index_out] == s1Count[index_out]:
                matches += 1
            elif s2Count[index_out] + 1 == s1Count[index_out]:
                matches -= 1

        return matches == 26