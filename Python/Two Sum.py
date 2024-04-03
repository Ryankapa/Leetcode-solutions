#Link ref https://leetcode.com/problems/two-sum/

class Solution:
    def twosum(numbers, target):
        numbers_length = len(numbers)
        for i in range(numbers_length - 1):
            for j in range(i + 1, numbers_length):
                if numbers[i] + numbers[j] == target:
                    return [i, j]
        return []
                

numbers = [3,3]
target = 6
test = Solution.twosum(numbers, target)
print(test)