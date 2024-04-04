class Solution:
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        if x > 0 and x < 10:
            return True
        reversed_x = str(x)[::-1]
        if int(reversed_x) == x:
            return True
        else:
            return False
        

x = 3121213
test = Solution.isPalindrome(x)
print(test)