class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for char in range(len(s)):
            
            rotated_string = s[char:] + s[:char] 
            if rotated_string == goal:
                return True 
            
        return False
    
sol = Solution()
print(sol.rotateString("abcde", "cdeab"))
    