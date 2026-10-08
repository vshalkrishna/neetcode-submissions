class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize res as an integer (0) instead of an empty string
        res = 0 
        
        for ch in s:
            res ^= ord(ch) # Convert character to integer and XOR
            
        for ch in t:
            res ^= ord(ch) # Convert character to integer and XOR
            
        # Convert the final integer result back to a string character
        return chr(res)