class Solution(object):
    def isPalindrome(self, x = int):
        """
        :type x: int
        :rtype: bool
        """
        rem = []
        n = x
        i=0
        while n > 0:
            reminder = n % 10
            n = n // 10
            rem.append(str(reminder))

        joined_value = "".join(rem)
        if str(x) == joined_value:
            return True
        return False
    
sol = Solution()
print(sol.isPalindrome(122))
