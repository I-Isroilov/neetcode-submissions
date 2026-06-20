class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr = "".join(ch.lower() for ch in s if ch.isalnum())
        return cleanedStr == cleanedStr[::-1]
      

        