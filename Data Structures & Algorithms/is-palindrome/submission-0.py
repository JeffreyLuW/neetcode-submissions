class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()

        n = len(clean)
        for i in range(n // 2):
            if clean[i] != clean[n - 1 - i]:
                return False
        return True
