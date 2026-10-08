class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = []
        s = s.lower()
        for i in range(len(s)):
            if s[i].isalnum():
                palindrome.append(s[i])
        low = 0
        high = len(palindrome)-1
        while low <= high :
            if palindrome[low] != palindrome[high]:
                return False
            low += 1
            high -= 1
        return True