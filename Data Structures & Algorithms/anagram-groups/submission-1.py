class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            signature = "".join(sorted(word))

            anagram_groups[signature].append(word)

        return list(anagram_groups.values())